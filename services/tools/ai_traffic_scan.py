#!/usr/bin/env python3
"""Find AI-service traffic in DNS, proxy or firewall logs.

Reads one or more customer-provided log exports (plain text or CSV), finds
connections to known AI services, and reports which hosts talked to which
services and how often. Passive and offline: it only reads files you give it.

Usage:
  python3 ai_traffic_scan.py LOG [LOG ...]            # summary table
  python3 ai_traffic_scan.py LOG --csv out.csv         # also write a CSV
  python3 ai_traffic_scan.py LOG --src-column client_ip --domain-column query

Plain-text logs: the first IPv4 address on a line is treated as the source
host. CSV logs: source and domain columns are auto-detected from common
header names, or set with --src-column / --domain-column.
"""

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

# (service name, regex matched against the full hostname)
AI_SERVICES = [
    ("OpenAI API", r"(^|\.)api\.openai\.com$"),
    ("ChatGPT", r"(^|\.)(chatgpt\.com|chat\.openai\.com|oaiusercontent\.com)$"),
    ("Anthropic API", r"(^|\.)api\.anthropic\.com$"),
    ("Claude", r"(^|\.)claude\.ai$"),
    ("Google Gemini API", r"(^|\.)generativelanguage\.googleapis\.com$"),
    ("Google Gemini app", r"(^|\.)gemini\.google\.com$"),
    ("Google Vertex AI", r"(^|\.)([a-z0-9-]+-)?aiplatform\.googleapis\.com$"),
    ("Azure OpenAI", r"\.openai\.azure\.com$"),
    ("Azure AI services", r"\.services\.ai\.azure\.com$"),
    ("Microsoft Copilot", r"(^|\.)copilot\.microsoft\.com$"),
    ("GitHub Copilot", r"(^|\.)(api\.githubcopilot\.com|copilot-proxy\.githubusercontent\.com)$"),
    ("AWS Bedrock", r"(^|\.)bedrock(-runtime|-agent-runtime)?\.[a-z0-9-]+\.amazonaws\.com$"),
    ("Mistral", r"(^|\.)api\.mistral\.ai$"),
    ("Cohere", r"(^|\.)api\.cohere\.(ai|com)$"),
    ("Groq", r"(^|\.)api\.groq\.com$"),
    ("Perplexity", r"(^|\.)api\.perplexity\.ai$"),
    ("Together AI", r"(^|\.)api\.together\.(xyz|ai)$"),
    ("Hugging Face", r"(^|\.)(huggingface\.co|hf\.co)$"),
    ("Replicate", r"(^|\.)api\.replicate\.com$"),
    ("OpenRouter", r"(^|\.)openrouter\.ai$"),
    ("DeepSeek", r"(^|\.)api\.deepseek\.com$"),
    ("xAI", r"(^|\.)api\.x\.ai$"),
    ("Cursor", r"(^|\.)cursor\.sh$"),
    ("Codeium / Windsurf", r"(^|\.)codeium\.com$"),
]
COMPILED = [(name, re.compile(rx, re.I)) for name, rx in AI_SERVICES]

HOST_RE = re.compile(r"(?<![\w.-])((?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,})(?![\w-])", re.I)
IPV4_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
SRC_HEADERS = ["src", "src_ip", "source", "source_ip", "client", "client_ip", "c-ip", "host", "srcaddr", "computer"]
DOMAIN_HEADERS = ["domain", "query", "qname", "dest_host", "dst_host", "hostname", "url", "cs-host", "server", "destination"]


def classify(hostname):
    host = hostname.lower().rstrip(".")
    for name, rx in COMPILED:
        if rx.search(host):
            return name
    return None


def hosts_in(text):
    for m in HOST_RE.finditer(text):
        yield m.group(1)


def scan_text(path, hits):
    with open(path, errors="replace") as f:
        for line in f:
            src_match = IPV4_RE.search(line)
            src = src_match.group(0) if src_match else "unknown"
            for h in hosts_in(line):
                svc = classify(h)
                if svc:
                    hits[(src, svc, h.lower().rstrip("."))] += 1


def pick(headers, wanted, override):
    if override:
        if override not in headers:
            sys.exit(f"Column '{override}' not found. Columns: {', '.join(headers)}")
        return override
    lower = {h.lower(): h for h in headers}
    for w in wanted:
        if w in lower:
            return lower[w]
    return None


def scan_csv(path, hits, src_col, dom_col):
    with open(path, newline="", errors="replace") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        s = pick(headers, SRC_HEADERS, src_col)
        d = pick(headers, DOMAIN_HEADERS, dom_col)
        for row in reader:
            src = (row.get(s) or "unknown").strip() if s else "unknown"
            text = row.get(d, "") if d else " ".join(v or "" for v in row.values())
            for h in hosts_in(text):
                svc = classify(h)
                if svc:
                    hits[(src, svc, h.lower().rstrip("."))] += 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("logs", nargs="+", type=Path)
    ap.add_argument("--csv", type=Path, help="write detailed results to this CSV file")
    ap.add_argument("--src-column", help="CSV column holding the source host")
    ap.add_argument("--domain-column", help="CSV column holding the domain or URL")
    args = ap.parse_args()

    hits = defaultdict(int)
    for path in args.logs:
        if not path.is_file():
            sys.exit(f"Not a file: {path}")
        if path.suffix.lower() == ".csv":
            scan_csv(path, hits, args.src_column, args.domain_column)
        else:
            scan_text(path, hits)

    if not hits:
        print("No traffic to known AI services found.")
        return

    by_src = defaultdict(lambda: defaultdict(int))
    for (src, svc, _), n in hits.items():
        by_src[src][svc] += n

    print(f"AI-service traffic found from {len(by_src)} source host(s)\n")
    print(f"{'Source host':<20} {'AI service':<22} {'Requests':>8}")
    print("-" * 52)
    for src in sorted(by_src, key=lambda s: -sum(by_src[s].values())):
        for svc, n in sorted(by_src[src].items(), key=lambda kv: -kv[1]):
            print(f"{src:<20} {svc:<22} {n:>8}")
    print("\nNext: confirm each source host’s role (engineering workstation, jump host, OT DMZ server)")
    print("and whether each service is approved. Add every confirmed AI system to the risk register.")

    if args.csv:
        with open(args.csv, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["source_host", "ai_service", "hostname", "requests"])
            for (src, svc, host), n in sorted(hits.items()):
                w.writerow([src, svc, host, n])
        print(f"\nDetailed results written to {args.csv}")


if __name__ == "__main__":
    main()
