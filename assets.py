# minify_assets.py
"""
Minify HTML, CSS, and JS files (Basic version)
"""

def minify_file(filename):
    if not Path(filename).exists():
        return
    print(f"📦 Minifying {filename}...")
    # Basic minification (you can improve this later)
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    # Remove extra whitespace
    content = " ".join(content.split())
    with open(f"minified_{filename}", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Created minified_{filename}")

if __name__ == "__main__":
    from pathlib import Path
    minify_file("index.html")
    minify_file("style.css")
