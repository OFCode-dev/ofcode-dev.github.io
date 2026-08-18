# SOUL.md — ofcodedev.me

Identity, purpose, and voice. Read this before making design or content decisions on the site.

## Purpose
This site is Omer Faruk Bayrak's professional front door: a portfolio proving shipped work, not a showcase of ambition. Every project listed here should be something a visitor can actually try today (store link, live page, working demo).

## Voice
Direct, technical, understated. Section titles are plain ("How I Think", "Capabilities"), not marketing copy. No hype language, no "revolutionary" or "cutting-edge" framing — let the shipped product speak.

## Principles
- **Ship, then show.** A project earns a homepage slot only once it's live and usable. Incomplete or paused projects go to a private repo, not a "coming soon" card.
- **One template, many members.** The Screenshot → Clipboard family reuses one visual template (Stitch's) across all members. Consistency across sibling products matters more than each one having a distinct look.
- **Clean authorship.** Git history reflects Omer Faruk Bayrak as author. No AI/Claude co-author attribution in commits — this was deliberately scrubbed once (Jul 2026) and should not reappear.
- **Static and simple.** No frameworks, no build pipeline, no unnecessary dependencies. Plain HTML/CSS is a feature, not a limitation — it keeps the site fast, portable, and easy to reason about.
- **Curate, don't accumulate.** The homepage is periodically pruned (see "Portfolio curation policy" in `MEMORY.md`) rather than left to grow indefinitely with every side project.

## When extending this site
- New extension family members: copy the Stitch template exactly (index.html + `/privacy/` + `/support/`), swap accent color, then integrate into the homepage family section.
- New blog posts go under `blog/<slug>/index.html`, sharing `blog/blog.css`; keep the "Signal & System" tone — analytical, first-person, no filler intro paragraphs.
- Before featuring anything new on the homepage, confirm it's actually live (store-approved, deployed, reachable) — not just code-complete.
