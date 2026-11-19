# Website

Static, single-page site for Preceptor Defense. No build step.

**Preview:** https://claude.ai/artifact/7gGmFkhDAgj7Rctqfm7wbB (private until shared).

## Before going live
- Replace `[email]` in `index.html` with your real address.
- Confirm the company name is cleared (`../research/name-check.md`) and buy the domain.

## Deploy on Netlify
1. Netlify: **Add new site → Import an existing project → GitHub**, pick this repo.
2. Set **Base directory** to `website`. `netlify.toml` publishes that folder; there is no build command.
3. Deploy, then open **Forms** and enable form detection. Submissions from the contact form appear under **Forms → contact**. Turn on email notifications there.
4. Add your domain under **Domain management**.

The contact form posts to Netlify Forms. Anywhere else (including the preview link), it shows a message asking people to email instead.
