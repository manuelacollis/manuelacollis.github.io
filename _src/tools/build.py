#!/usr/bin/env python3
"""
Site builder for manuelacollis.com.

Reads _src/content/site.yml + _src/templates/*.j2 and writes generated
HTML, redirect folders, sitemap, and robots.txt directly to the git repo
root (the parent folder of _src/).

Layout:
  <repo>/
    _src/
      content/site.yml     <-- edit this
      templates/*.j2       <-- edit rarely
      tools/build.py       <-- this file
      PROMPTS.md           <-- cheat sheet
    files/                 <-- paper PDFs + CV.pdf
    assets/                <-- styles.css, portrait.jpg, cv/*.png, favicons, og-image
    <slug>/index.html      <-- built redirect folders (about/, wtp/, ...)
    *.html                 <-- built pages (index/research/cv/404)

Usage:
  cd ~/Documents/GitHub/manuelacollis.github.io
  python3 _src/tools/build.py

After it finishes:
  git add -A
  git commit -m "Update"
  git push origin master
"""
import base64
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: python3 -m pip install -r _src/tools/requirements.txt")
try:
    from jinja2 import Environment, FileSystemLoader, StrictUndefined
except ImportError:
    sys.exit("Jinja2 required: python3 -m pip install -r _src/tools/requirements.txt")
try:
    import markdown as md_lib
except ImportError:
    sys.exit("markdown required: python3 -m pip install -r _src/tools/requirements.txt")


# ---------- paths ----------
SRC = Path(__file__).resolve().parent.parent    # _src/
REPO = SRC.parent                                # repo root (~/Documents/GitHub/manuelacollis.github.io)


# ---------- markdown helpers ----------
def md_inline(text: str) -> str:
    if text is None:
        return ""
    html = md_lib.markdown(text.strip(), extensions=["extra"])
    m = re.fullmatch(r"<p>(.*?)</p>", html, re.DOTALL)
    return m.group(1) if m else html


def md_block(text: str) -> str:
    if text is None:
        return ""
    return md_lib.markdown(text.strip(), extensions=["extra"])


def b64(s: str) -> str:
    return base64.b64encode(s.encode("utf-8")).decode("ascii")


# ---------- content loading ----------
def load_content() -> dict:
    with (SRC / "content" / "site.yml").open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def find_cv_pages() -> list:
    cv_dir = REPO / "assets" / "cv"
    if not cv_dir.exists():
        return []
    return [
        {"path": f"assets/cv/{p.name}", "v": int(p.stat().st_mtime)}
        for p in sorted(cv_dir.glob("cv-page-*.png"))
    ]


def preprocess(data: dict) -> dict:
    p = data.get("person", {})
    user = p.get("email_user", "")
    domain = p.get("email_domain", "")
    data["email_u"] = b64(user)
    data["email_d"] = b64(domain)
    data["email_fallback"] = (
        user.replace(".", "&nbsp;[dot]&nbsp;")
        + "&nbsp;[at]&nbsp;"
        + domain.replace(".", "&nbsp;[dot]&nbsp;")
    )

    home = data.get("home", {})
    home["about_html"] = md_block(home.get("about", ""))

    for tile in data.get("contact_tiles", []):
        if tile.get("type") == "email":
            continue
        val = (tile.get("value") or "").strip()
        lines = [md_inline(ln) for ln in val.splitlines() if ln.strip()]
        tile["value_html"] = "<br/>".join(lines)

    research = data.get("research", {})
    research["intro_html"] = md_inline(research.get("intro", ""))
    for bucket in ("publications", "working_papers", "work_in_progress"):
        for paper in research.get(bucket, []) or []:
            paper["abstract_html"] = md_inline(paper.get("abstract", ""))
            paper["authors_html"] = md_inline(paper.get("authors", ""))
            paper["venue_html"] = md_inline(paper.get("venue", ""))

    cv = data.get("cv", {})
    cv["intro_html"] = md_inline(cv.get("intro", ""))
    cv["pages"] = find_cv_pages()
    pdf_full = REPO / cv.get("pdf_path", "")
    cv["pdf_v"] = int(pdf_full.stat().st_mtime) if pdf_full.exists() else 0

    return data


# ---------- redirect targets ----------
REDIRECTS = {
    "about":        "/",
    "cv":           "/cv.html",
    "research":     "/research.html",
    "publications": "/research.html",
}


def _all_slugs(data: dict) -> set:
    slugs = set(REDIRECTS.keys())
    slugs |= set(paper_short_urls(data).keys())
    return {s.lower() for s in slugs}


def paper_short_urls(data: dict) -> dict:
    redirects = {}
    HOST_STRIP = (
        "https://manuelacollis.com", "http://manuelacollis.com",
        "https://manuelacollis.github.io", "http://manuelacollis.github.io",
    )
    research = data.get("research", {})
    for bucket in ("publications", "working_papers", "work_in_progress"):
        for paper in research.get(bucket, []) or []:
            slug_field = paper.get("short_url")
            if not slug_field:
                continue
            slugs = [slug_field] if isinstance(slug_field, str) else list(slug_field)
            target = None
            for link in paper.get("links") or []:
                url = link.get("url", "")
                if url.lower().endswith(".pdf"):
                    target = url
                    break
            if not target:
                print(f"  WARN: paper {paper.get('title')!r} has short_url "
                      f"{slugs!r} but no .pdf link — skipping")
                continue
            for host in HOST_STRIP:
                if target.startswith(host):
                    target = target[len(host):]
                    break
            if not target.startswith("/"):
                target = "/" + target
            for slug in slugs:
                redirects[slug] = target
    return redirects


def write_redirect(slug: str, target: str) -> None:
    """Write REPO/<slug>/index.html — served as manuelacollis.com/<slug>/."""
    out_dir = REPO / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Redirecting…</title>
  <meta http-equiv="refresh" content="0; url={target}" />
  <link rel="canonical" href="{target}" />
  <meta name="robots" content="noindex" />
  <script>window.location.replace({target!r});</script>
</head>
<body>
  <p>If you are not redirected, <a href="{target}">click here</a>.</p>
</body>
</html>
"""
    (out_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"  wrote {slug}/index.html  ->  {target}")


# ---------- cleanup of stale redirect folders at repo root ----------
# Any top-level folder in this set is definitely NOT a redirect and should
# never be scanned/cleaned. Everything else is inspected.
SKIP_DIRS = {
    "_src", "assets", "files", ".git", ".github",
    "shortcuts",           # legacy intermediate, if it still exists
    "__pycache__", "node_modules",
}


def _looks_like_redirect_folder(entry: Path) -> bool:
    contents = list(entry.iterdir())
    if len(contents) != 1 or contents[0].name != "index.html":
        return False
    text = contents[0].read_text(encoding="utf-8", errors="ignore")
    return 'http-equiv="refresh"' in text


def clean_stale_redirects(current_slugs: set) -> None:
    """Delete redirect folders at REPO root not in the current build."""
    for entry in REPO.iterdir():
        if not entry.is_dir():
            continue
        if entry.name in SKIP_DIRS or entry.name.startswith("."):
            continue
        if entry.name in current_slugs:
            continue
        if _looks_like_redirect_folder(entry):
            try:
                (entry / "index.html").unlink()
                entry.rmdir()
                print(f"  cleaned stale redirect: {entry.name}/")
            except OSError as e:
                print(f"  (skipped cleanup of {entry.name}/: {e})")

    # Also nuke legacy shortcuts/ intermediate folder if it lingers.
    shortcuts = REPO / "shortcuts"
    if shortcuts.exists() and shortcuts.is_dir():
        try:
            for sub in shortcuts.iterdir():
                if sub.is_dir():
                    for f in sub.iterdir():
                        f.unlink()
                    sub.rmdir()
                else:
                    sub.unlink()
            shortcuts.rmdir()
            print("  cleaned legacy shortcuts/ intermediate")
        except OSError as e:
            print(f"  (skipped cleanup of shortcuts/: {e})")


# ---------- page rendering ----------
def render_pages(data: dict) -> None:
    env = Environment(
        loader=FileSystemLoader(SRC / "templates"),
        autoescape=False,
        keep_trailing_newline=True,
        undefined=StrictUndefined,
    )
    pages = [
        ("index.html", "index.html.j2", "home", {
            "page_title": f"{data['person']['name']} — Assistant Professor, CMU Heinz College",
            "page_description": data["home"]["meta_description"].strip(),
            "page_path": "",
        }),
        ("research.html", "research.html.j2", "research", {
            "page_title": f"Research — {data['person']['name']}",
            "page_description": data["research"]["meta_description"].strip(),
            "page_path": "research.html",
        }),
        ("cv.html", "cv.html.j2", "cv", {
            "page_title": f"CV — {data['person']['name']}",
            "page_description": data["cv"]["meta_description"].strip(),
            "page_path": "cv.html",
        }),
        ("404.html", "404.html.j2", "404", {
            "page_title": f"Page not found — {data['person']['name']}",
            "page_description": "The page you’re looking for doesn’t exist.",
            "page_path": "404.html",
            "known_slugs": sorted(_all_slugs(data)),
        }),
    ]
    for out_name, tmpl, page_id, extra in pages:
        html = env.get_template(tmpl).render(**{**data, **extra, "page": page_id})
        (REPO / out_name).write_text(html, encoding="utf-8")
        print(f"  wrote {out_name}")


# ---------- CV preview regeneration ----------
def regenerate_cv_previews_if_needed() -> None:
    """If the CV PDF is newer than the PNG previews, rebuild them.

    So the workflow to update the CV becomes: drop new CV_Manuela_Collis.pdf
    into files/, run build.py — previews auto-refresh.
    """
    pdf = REPO / "files" / "CV_Manuela_Collis.pdf"
    cv_dir = REPO / "assets" / "cv"
    if not pdf.exists():
        print("  (no CV PDF at files/CV_Manuela_Collis.pdf — skipping)")
        return
    first_png = cv_dir / "cv-page-01.png"
    if first_png.exists() and first_png.stat().st_mtime >= pdf.stat().st_mtime:
        print("  CV previews are up to date.")
        return
    try:
        import fitz  # pymupdf
    except ImportError:
        print("  (pymupdf not installed — skipping. Install: python3 -m pip install pymupdf)")
        return
    print(f"  CV PDF is newer than previews — regenerating from {pdf.name} ...")
    cv_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(str(pdf))
    zoom = 2.0
    mat = fitz.Matrix(zoom, zoom)
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        png = pix.tobytes("png")
        out = cv_dir / f"cv-page-{i:02d}.png"
        with open(out, "wb") as f:
            f.write(png)
        print(f"    wrote assets/cv/{out.name}  ({out.stat().st_size} bytes)")


# ---------- sitemap + robots ----------
def write_sitemap_and_robots(data: dict) -> None:
    import datetime
    base = data["site"]["url"].rstrip("/")
    today = datetime.date.today().isoformat()
    urls = ["", "research.html", "cv.html"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = f"{base}/{u}".rstrip("/")
        sm.append(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod></url>")
    sm.append("</urlset>")
    (REPO / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    print("  wrote sitemap.xml")

    robots = (
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {base}/sitemap.xml\n"
    )
    (REPO / "robots.txt").write_text(robots, encoding="utf-8")
    print("  wrote robots.txt")


# ---------- main ----------
def main() -> None:
    print(f"Building site")
    print(f"  source: {SRC}")
    print(f"  output: {REPO}")
    print("")
    print("Regenerating CV previews if needed...")
    regenerate_cv_previews_if_needed()
    print("")
    print("Rendering pages...")
    data = preprocess(load_content())
    render_pages(data)
    print("")
    print("Writing redirects...")
    paper_redirects = paper_short_urls(data)
    current_slugs = set(REDIRECTS) | set(paper_redirects)
    clean_stale_redirects(current_slugs)
    for slug, target in REDIRECTS.items():
        write_redirect(slug, target)
    for slug, target in paper_redirects.items():
        write_redirect(slug, target)
    print("")
    print("Writing sitemap & robots...")
    write_sitemap_and_robots(data)
    print("")
    print("Done. Ready to commit and push:")
    print("  cd " + str(REPO))
    print("  git add -A && git commit -m \"Update\" && git push origin master")


if __name__ == "__main__":
    main()
