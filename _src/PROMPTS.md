# Update prompts — paste into Claude / Cursor / Codex

A cheat sheet for updating manuelacollis.com without having to remember
where things live. Pick a prompt, fill in the bracketed bits, paste into
a fresh AI session that has access to your git repo, and let it handle
the file edits + build + commit + push.

---

## How the site is organized

Everything lives inside the git repo at `~/Documents/GitHub/manuelacollis.github.io/`.

- Single source of editable content: `_src/content/site.yml`
- Page templates (Jinja2): `_src/templates/*.html.j2`
- Build script: `_src/tools/build.py`
- Paper PDFs and CV: `files/` (drop new files here directly)
- Styles: `assets/styles.css` (edit directly — ships as-is)
- Generated at repo root: `index.html`, `research.html`, `cv.html`, `404.html`,
  `sitemap.xml`, `robots.txt`, all shortcut folders (`about/`, `wtp/`, etc.)

## The workflow

After ANY content edit:

```
cd ~/Documents/GitHub/manuelacollis.github.io
python3 _src/tools/build.py
git add -A
git commit -m "Describe your change"
git push origin master
```

Live at `https://manuelacollis.com` in about 60 seconds.

---

## Add a journal publication

> Add a new publication to `_src/content/site.yml` under `research.publications`
> (top of the list so it appears first):
>
> - Title: **[title]**
> - Co-authors: **[names]** (with Google Scholar or personal-site URLs where possible)
> - Venue: **[journal, volume(issue): pages, year]** — italicize journal with single asterisks
> - Abstract: **[full abstract]**
> - Final PDF URL: **[URL to the PDF you dropped into files/]**
> - DOI: **[doi]**
> - Replication files (if any): **[URL]**
> - Short URL slug (optional, lowercase): **[slug]**
>
> Also generate a BibTeX entry following the pattern of existing ones
> (citekey `lastname1_lastname2_year_keyword`, `@article{...}` style with aligned fields).
> Then run `python3 _src/tools/build.py` and confirm the publication appears on research.html.

## Add a working paper

> Add a new working paper to `_src/content/site.yml` under `research.working_papers`:
>
> - Title: **[title]**
> - Co-authors (if any): **[names with links]**
> - Tag (optional — "Submitted", "Under review", "R&R at *Journal*"): **[tag or omit]**
> - Abstract: **[paste]**
> - Paper draft URL (if shareable): **[URL to PDF in files/]**
> - Pre-registration URL: **[URL]**
> - Short URL slug (optional, lowercase): **[slug]**
> - Note (if no shareable draft): "Draft available upon request."
>
> Generate a `@unpublished{...}` BibTeX entry with citekey
> `collis_keyword_year` or `collis_coauthor_keyword_year`. Then build.

## Update an existing paper (drop-in replacement)

> The paper titled **[title]** has an updated PDF. Same filename:
>   1. Replace `files/[FILENAME].pdf` with the new PDF (same name)
>   2. `git add files/ && git commit -m "Update [title] paper" && git push origin master`
>
> No build.py needed — the site links to that filename and everything else stays the same.

## Update an existing paper (new filename)

> The paper titled **[title]** has an updated PDF with a new filename:
>   1. Drop new `[NEW_FILENAME].pdf` into files/
>   2. In `_src/content/site.yml`, find the paper and update the `url` field under
>      `links` from the old filename to the new one
>   3. Run `python3 _src/tools/build.py`
>   4. `git add -A && git commit -m "Update [title] paper" && git push origin master`

## Promote a paper (WIP → Working Paper → Publication)

> Move the paper titled **[title]** in `_src/content/site.yml`:
>
> From: `research.[work_in_progress | working_papers]`
> To:   `research.[working_papers | publications]`
>
> If moving to publications, ask me for the venue (journal name, volume, issue,
> pages, year, DOI) and the final PDF URL. Update the BibTeX entry from
> `@unpublished` to `@article` and fill in the new fields. Then build + push.

## Replace the CV

> Replace `files/CV_Manuela_Collis.pdf` with the new PDF I attached.
> `python3 _src/tools/build.py` — it auto-detects the newer PDF and regenerates
> the page-preview PNGs in `assets/cv/`. Then commit + push.

## Add a short URL for an existing paper

> In `_src/content/site.yml`, add a `short_url: "[slug]"` line under the paper
> titled **[title]**. Slug must be lowercase — the 404 page has a smart-redirect
> that catches any case mismatch (/WTP → /wtp).
> Then `python3 _src/tools/build.py`, commit + push.

## Update the bio

> Edit the `home.about` block in `_src/content/site.yml`. Keep the existing
> paragraph structure. Markdown links work — use `[text](https://url)`.
> Then build + commit + push.

## Update the hero tagline

> Edit `home.hero_lede` in `_src/content/site.yml`. Keep it under ~25 words.
> Also update `home.meta_description` to match if the substantive content
> changed — it's used for SEO and social preview cards. Then build + commit + push.

## Change the email address

> Update `person.email_user` and `person.email_domain` in `_src/content/site.yml`.
> The build script base64-encodes both — no other files need editing.
> Then build + commit + push.

## Update the social preview image (OG card)

> Regenerate `assets/og-image.jpg`. Spec:
> - 1200 x 630 px, JPEG quality 88, progressive
> - Carnegie Red (#c41230) left stripe, 8px wide
> - Portrait on the right (cropped 4:5 from `_src/assets/portrait-original.jpg`)
> - Left side text (top→bottom): red uppercase eyebrow "CARNEGIE MELLON UNIVERSITY",
>   serif-bold "Manuela R. Collis", subtitle lines "Assistant Professor" and "Heinz College",
>   footer "manuelacollis.com" in muted gray
>
> Use Pillow + DejaVuSerif fonts. Then commit `assets/og-image.jpg`.

---

## Conventions when editing _src/content/site.yml

- **Markdown links** work inside any string field: `[text](url)`.
- **Multi-line text** uses YAML block scalar with leading `|`.
- **List ordering matters** — papers appear in the order listed. Newest first.
- **Don't edit the rendered HTML files** at repo root — they're regenerated on every build.
- **Don't delete a paper's `bibtex:` field** unless it's in `work_in_progress`
  (those papers don't get a Copy BibTeX button).
- **`short_url` slugs must be lowercase**, hyphen-separated, and not collide
  with reserved folder names (`about`, `publications`, `cv`, `research`).

## Safety net (if something goes wrong after push)

Two recovery points were created before the initial rewrite:

- Git tag: `pre-static-rewrite-2026-06-23`
- Branch:  `jekyll-archive`

To roll the whole site back to the pre-rewrite Jekyll version:

```
cd ~/Documents/GitHub/manuelacollis.github.io
git reset --hard pre-static-rewrite-2026-06-23
git push --force-with-lease origin master
```

To undo the most recent change (before pushing):

```
git reset --hard HEAD~1
```

To undo the most recent change (after pushing):

```
git revert HEAD
git push
```
