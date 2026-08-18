# MEMORY.md — ofcode-dev.github.io

Project facts and state. Update when structure or decisions change; don't log routine edits.

## What this is
Static GitHub Pages site for Omer Faruk Bayrak (GitHub @OFCode-dev). Personal portfolio + blog.
- Custom domain: `ofcodedev.me` (via CNAME), `.nojekyll` present (no Jekyll processing).
- Contact: contact@ofcodedev.me.
- No build step — plain HTML/CSS, hand-authored, no framework.

## Structure
- `index.html` — homepage. Sections: Hero, Screenshot → Clipboard Family, Featured Work (Quick Web Notepad), How I Think, Capabilities, Contact & Links.
- `blog/` — blog "Signal & System" (renamed from earlier title 2026-08). `blog/index.html` + one post per subdirectory (e.g. `blog/how-ai-can-confidently-explain-the-wrong-answer/`). Shared `blog/blog.css`.
- `data/dates.json` — public data endpoint at `/data/dates.json`, published 2026-07-08.
- `stitch-screenshot-clipboard/`, `osmanli-turkcesi-klavye-destegi/`, `swiftkey-osmanli-turkcesi/` — standalone campaign/landing sub-sites, each self-contained.
- `swiftkey-osmanli-turkcesi/index.html` is currently **untracked** (new, not yet committed as of 2026-08-18).

## Screenshot → Clipboard extension family
Three sibling browser extensions, each with its own repo, all featured together in one homepage section (not separately):
- Quick Screenshot → Clipboard (Chrome + Firefox, live in stores)
- Stitch Screenshot → Clipboard (established template source)
- Frame Screenshot → Clipboard (video frame → clipboard; launched Aug 2026)

Each ships landing pages replicated from the Stitch template: single `index.html` with inline CSS, dark theme support, `/privacy/` and `/support/` sub-pages. New family members should follow this same template for consistency.

## Portfolio curation policy
Homepage only features **shipped, complete** projects. Incomplete/unreleased projects (wouldyouratherapp, zoomwheelapp) were archived to private repos rather than listed — decided Aug 2026.

## Recent history (chronological, from git log)
- Jun 2026: Built Ottoman Turkish SwiftKey campaign page (client-side, role-based request generator).
- Jul 2026: Removed AI/Claude co-author attributions from git history across OFCode-dev repos; standardized git identity.
- Aug 2026: Extension family relaunch — Frame shipped, portfolio reorganized around the 3-extension family, unfinished projects archived, `dates.json` published, blog section added and later rebranded to "Signal & System".

## Open threads
- SwiftKey Ottoman Turkish campaign page work (`swiftkey-osmanli-turkcesi/`) has uncommitted new content — verify locally before treating as production-ready.
