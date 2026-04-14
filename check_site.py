from pathlib import Path
import sys

site = Path(__file__).with_name("index.html")
errors = []

if not site.exists():
    errors.append("Missing index.html")
else:
    html = site.read_text(encoding="utf-8")

    required_ids = ["home", "about", "skills", "projects", "resume", "contact"]
    for section_id in required_ids:
        if f'id="{section_id}"' not in html:
            errors.append(f"Missing section: {section_id}")

    for heading in ["Technical Skills", "Business Skills", "Tools"]:
        if heading not in html:
            errors.append(f"Missing skills heading: {heading}")

    project_labels = [
        "Problem",
        "Data",
        "Approach",
        "Outcome / Impact",
        "Your Contribution",
    ]
    for label in project_labels:
        if html.count(f"<dt>{label}</dt>") < 2:
            errors.append(f"Expected project label twice: {label}")

    if 'href="styles.css"' not in html:
        errors.append("Missing stylesheet link")

    css = Path(__file__).with_name("styles.css")
    if not css.exists():
        errors.append("Missing styles.css")
    else:
        css_text = css.read_text(encoding="utf-8")
        if "@media (max-width: 720px)" not in css_text:
            errors.append("Missing mobile media query")

    resume = Path(__file__).with_name("CV - MA Yuyang.pdf")
    if not resume.exists():
        errors.append("Missing PDF resume")

if errors:
    print("\n".join(errors))
    sys.exit(1)
