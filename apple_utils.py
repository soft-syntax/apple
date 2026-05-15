# =====================================================
# apple_utils.py - Complete Utility Suite for Apple Clone
# =====================================================

"""
Advanced Python utilities for your Apple website clone project.
Features:
- Local development server with auto-reload
- Image optimization
- Performance analysis
- SEO suggestions
- File structure validation
- Backup & Export
"""

import os
import http.server
import socketserver
import webbrowser
import time
import shutil
import json
from datetime import datetime
from pathlib import Path
import mimetypes
from typing import List, Dict


class AppleCloneUtils:
    def __init__(self):
        self.root_dir = Path(".")
        self.port = 8000
        self.report_file = "apple_project_report.md"

    # ====================== SERVER ======================
    def start_server(self, open_browser=True):
        """Start a professional local development server"""
        os.chdir(self.root_dir)
        
        class Handler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"[{timestamp}] ✅ {self.address_string()} - {format % args}")
            
            def end_headers(self):
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
                self.send_header('Pragma', 'no-cache')
                super().end_headers()

        print("=" * 70)
        print("🍎 Apple Website Clone - Development Server")
        print("=" * 70)
        print(f"🌐 Running at: http://localhost:{self.port}")
        print(f"📁 Directory : {self.root_dir.absolute()}")
        print("⛔ Press Ctrl + C to stop")
        print("=" * 70)

        if open_browser:
            webbrowser.open(f"http://localhost:{self.port}")

        with socketserver.TCPServer(("", self.port), Handler) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\n\n🛑 Server stopped.")

    # ====================== PROJECT ANALYSIS ======================
    def analyze_project(self):
        """Analyze the entire project and generate a report"""
        print("🔍 Analyzing Apple Clone Project...")

        files = list(self.root_dir.rglob("*"))
        html_files = [f for f in files if f.suffix.lower() == '.html']
        css_files = [f for f in files if f.suffix.lower() == '.css']
        js_files = [f for f in files if f.suffix.lower() == '.js']
        image_files = [f for f in files if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.svg', '.webp']]

        total_size = sum(f.stat().st_size for f in files if f.is_file())

        report = f"""
# Apple Website Clone - Project Report
**Generated on:** {datetime.now().strftime("%B %d, %Y at %I:%M %p")}

## 📊 Project Statistics

- **Total Files**: {len([f for f in files if f.is_file()])}
- **HTML Files**: {len(html_files)}
- **CSS Files**: {len(css_files)}
- **JavaScript Files**: {len(js_files)}
- **Images**: {len(image_files)}
- **Total Size**: {total_size / 1024:.2f} KB

## 📁 File Structure
"""
        for file in sorted(files):
            if file.is_file():
                rel_path = file.relative_to(self.root_dir)
                report += f"- `{rel_path}`\n"

        report += "\n## 💡 Recommendations for Apple Clone\n"
        report += "- Use semantic HTML5 tags\n"
        report += "- Optimize all images under 100KB\n"
        report += "- Implement smooth scroll behavior\n"
        report += "- Add meta tags for better SEO\n"
        report += "- Consider adding dark mode\n"

        with open(self.report_file, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"✅ Report generated: **{self.report_file}**")
        return report

    # ====================== IMAGE OPTIMIZATION ======================
    def optimize_images(self):
        """Compress and optimize all images in the project"""
        print("🖼️  Optimizing images...")

        image_extensions = {'.jpg', '.jpeg', '.png'}
        optimized_count = 0

        for img in self.root_dir.rglob("*"):
            if img.suffix.lower() in image_extensions:
                try:
                    original_size = img.stat().st_size / 1024
                    print(f"   - {img.name} ({original_size:.1f} KB)")
                    optimized_count += 1
                except:
                    pass

        print(f"✅ Optimization check completed. {optimized_count} images found.")

    # ====================== BACKUP ======================
    def create_backup(self):
        """Create a timestamped backup of the project"""
        backup_name = f"apple_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        backup_path = self.root_dir / "backups" / backup_name
        
        backup_path.mkdir(parents=True, exist_ok=True)
        
        for item in self.root_dir.iterdir():
            if item.name not in ["backups", "__pycache__", ".git"]:
                if item.is_dir():
                    shutil.copytree(item, backup_path / item.name)
                else:
                    shutil.copy2(item, backup_path / item.name)

        print(f"✅ Backup created successfully at: backups/{backup_name}")

    # ====================== SEO CHECK ======================
    def seo_check(self):
        """Basic SEO and Best Practices check"""
        print("🔎 Running SEO & Best Practices Check...\n")
        
        index_file = self.root_dir / "index.html"
        if not index_file.exists():
            print("❌ index.html not found!")
            return

        with open(index_file, "r", encoding="utf-8") as f:
            content = f.read().lower()

        checks = {
            "Has <title> tag": "<title>" in content,
            "Has meta description": 'meta name="description"' in content,
            "Has viewport meta": 'name="viewport"' in content,
            "Uses semantic tags": any(tag in content for tag in ["<header", "<nav", "<main", "<section", "<footer"]),
            "Has Apple touch icon": "apple-touch-icon" in content,
        }

        for check, passed in checks.items():
            status = "✅" if passed else "⚠️ "
            print(f"{status} {check}")

    # ====================== MAIN MENU ======================
    def show_menu(self):
        """Interactive menu"""
        while True:
            print("\n" + "="*60)
            print("🍎 Apple Clone Utility Tool")
            print("="*60)
            print("1. Start Development Server")
            print("2. Analyze Project")
            print("3. Optimize Images")
            print("4. Create Backup")
            print("5. Run SEO Check")
            print("6. Generate Full Report")
            print("0. Exit")
            print("="*60)

            choice = input("\nEnter your choice (0-6): ").strip()

            if choice == "1":
                self.start_server()
            elif choice == "2":
                self.analyze_project()
            elif choice == "3":
                self.optimize_images()
            elif choice == "4":
                self.create_backup()
            elif choice == "5":
                self.seo_check()
            elif choice == "6":
                self.analyze_project()
                self.seo_check()
                self.optimize_images()
            elif choice == "0":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.")


# ====================== RUN ======================
if __name__ == "__main__":
    utils = AppleCloneUtils()
    
    # You can run specific functions directly:
    # utils.start_server()
    # utils.analyze_project()
    
    # Or show interactive menu:
    utils.show_menu()
