from pathlib import Path
import markdown

SOURCE = Path("docs")
OUTPUT = Path("dist")

OUTPUT.mkdir(exist_ok=True)

for md_file in SOURCE.rglob("*.md"):
    rel = md_file.relative_to(SOURCE)

    url_path = rel.with_suffix("")

    target_dir = OUTPUT / url_path
    target_dir.mkdir(parents=True, exist_ok=True)

    html = markdown.markdown(
        md_file.read_text(encoding="utf-8"),
        extensions=["extra", "toc"]
    )

    page = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{url_path.name}</title>
</head>
<body>
{html}
</body>
</html>
"""

    (target_dir / "index.html").write_text(
        page,
        encoding="utf-8"
    )

print("Site generated")
