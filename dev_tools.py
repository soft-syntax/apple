# ========================================================
# apple_dev_tools.py - Complete Development Toolkit
# For Apple Website Clone by soft-syntax
# ========================================================

"""
Advanced Development Toolkit for Apple Website Clone.
This is a full-featured utility script with multiple tools.
"""

import os
import sys
import json
import shutil
import webbrowser
import http.server
import socketserver
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import mimetypes
import time
import hashlib


class AppleDevTools:
    def __init__(self):
        self.root = Path(".")
        self.config_file = self.root / "apple_config.json"
        self.log_file = self.root / "dev_logs.txt"
        self.port = 8000
        self.load_config()

    def load_config(self):
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    self.config = json.load(f)
            except:
                self.config = self.create_default_config()
        else:
            self.config = self.create_default_config()

    def create_default_config(self) -> dict:
        default = {
            "project_name": "Apple Website Clone",
            "version": "1.0.0",
            "author": "soft-syntax",
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "server": {
                "port": 8000,
                "auto_open_browser": True
            },
            "features": [
                "Responsive Navbar",
                "Hero Section",
                "Product Showcase",
                "Footer Links"
            ],
            "settings": {
                "dark_mode_supported": False,
                "animations_enabled": True
            }
        }
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(default, f, indent=4)
        return default

    def log(self, message: str, level: str = "INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry + "\n")
        except:
            pass

    # ====================== SERVER ======================
    def start_server(self):
        """Start local development server with enhanced logging"""
        os.chdir(self.root)
        self.log("Starting Apple Clone Development Server...", "START")

        class Handler(http.server.SimpleHTTPRequestHandler):
            def log_message(self, format, *args):
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"[{timestamp}] 🌐 {self.address_string()} - {format % args}")

            def end_headers(self):
                self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
                self.send_header("Pragma", "no-cache")
                super().end_headers()

        try:
            with socketserver.TCPServer(("", self.config["server"]["port"]), Handler) as httpd:
                url = f"http://localhost:{self.config['server']['port']}"
                print("\n" + "="*75)
                print("🍎 APPLE WEBSITE CLONE - DEVELOPMENT SERVER")
                print("="*75)
                print(f"🌐 Local URL     : {url}")
                print(f"📁 Serving Path  : {self.root.absolute()}")
                print(f"📄 Config File   : {self.config_file.name}")
                print("⛔ Press Ctrl+C to stop server")
                print("="*75 + "\n")

                if self.config["server"]["auto_open_browser"]:
                    webbrowser.open(url)

                httpd.serve_forever()
        except KeyboardInterrupt:
            self.log("Server stopped by user.", "STOP")
        except Exception as e:
            self.log(f"Server error: {e}", "ERROR")

    # ====================== PROJECT ANALYSIS ======================
    def analyze_project(self) -> Dict:
        """Deep analysis of the entire project"""
        self.log("Starting deep project analysis...")

        all_files = list(self.root.rglob("*"))
        files_only = [f for f in all_files if f.is_file()]

        stats = {
            "total_files": len(files_only),
            "total_size_kb": round(sum(f.stat().st_size for f in files_only) / 1024, 2),
            "html_files": len(list(self.root.rglob("*.html"))),
            "css_files": len(list(self.root.rglob("*.css"))),
            "js_files": len(list(self.root.rglob("*.js"))),
            "image_files": len([f for f in files_only if f.suffix.lower() in {'.png', '.jpg', '.jpeg', '.svg', '.webp'}]),
            "last_modified": datetime.fromtimestamp(max((f.stat().st_mtime for f in files_only), default=0)).strftime("%Y-%m-%d %H:%M")
        }

        self.save_analysis_report(stats)
        return stats

    def save_analysis_report(self, stats: Dict):
        report = f"""# Apple Clone Project Analysis Report
**Generated:** {datetime.now().strftime("%B %d, %Y at %I:%M %p")}

## 📊 Project Statistics
- Total Files: {stats['total_files']}
- Total Size: {stats['total_size_kb']} KB
- HTML Files: {stats['html_files']}
- CSS Files: {stats['css_files']}
- JavaScript Files: {stats['js_files']}
- Images: {stats['image_files']}

## 🕒 Last Modified: {stats['last_modified']}

## ✅ Recommendations
1. Keep images under 150KB each
2. Minify CSS and JS for production
3. Add alt texts to all images
4. Consider implementing lazy loading
5. Test thoroughly on mobile devices
"""

        with open("PROJECT_ANALYSIS.md", "w", encoding="utf-8") as f:
            f.write(report)
        print("✅ Detailed report saved as PROJECT_ANALYSIS.md")

    # ====================== SEO & ACCESSIBILITY ======================
    def seo_audit(self):
        """Basic SEO and Accessibility audit"""
        self.log("Running SEO & Accessibility Audit...")
        index_path = self.root / "index.html"
        
        if not index_path.exists():
            print("❌ index.html not found!")
            return

        content = index_path.read_text(encoding="utf-8").lower()

        audit = {
            "title_tag": "<title>" in content,
            "meta_description": 'meta name="description"' in content,
            "viewport": 'name="viewport"' in content,
            "og_tags": "og:" in content,
            "semantic_tags": any(x in content for x in ["<header", "<nav", "<main", "<section", "<footer"]),
            "apple_icons": "apple-touch-icon" in content,
        }

        print("\n🔍 SEO & Accessibility Audit Results:")
        for key, passed in audit.items():
            print(f"{'✅' if passed else '⚠️'} {key.replace('_', ' ').title()}")

    # ====================== BACKUP SYSTEM ======================
    def create_backup(self):
        """Create full backup with timestamp"""
        backup_dir = self.root / "backups"
        backup_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"apple_backup_{timestamp}"
        backup_path = backup_dir / backup_name

        shutil.copytree(self.root, backup_path, ignore=shutil.ignore_patterns(
            'backups', '__pycache__', '*.pyc', '.git'
        ))

        print(f"✅ Full backup created: backups/{backup_name}")

    # ====================== UTILITY FUNCTIONS ======================
    def list_all_files(self):
        print("\n📁 Project Files:")
        for file in sorted(self.root.rglob("*")):
            if file.is_file():
                size = f"{file.stat().st_size / 1024:.1f} KB"
                print(f"   {file.relative_to(self.root):<40} {size:>10}")

    def update_version(self):
        current = self.config.get("version", "1.0.0")
        print(f"Current version: {current}")
        new_version = input("Enter new version (e.g., 1.1.0): ").strip()
        
        if new_version:
            self.config["version"] = new_version
            self.config["last_updated"] = datetime.now().strftime("%Y-%m-%d")
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
            print(f"✅ Version updated to {new_version}")

    # ====================== MAIN MENU ======================
    def show_menu(self):
        while True:
            print("\n" + "="*80)
            print("🍎 APPLE CLONE DEVELOPMENT TOOLKIT")
            print("="*80)
            print("1.  Start Development Server")
            print("2.  Analyze Project")
            print("3.  Run SEO & Accessibility Audit")
            print("4.  Create Full Backup")
            print("5.  List All Project Files")
            print("6.  Update Project Version")
            print("7.  Setup Project Structure")
            print("8.  Show Config")
            print("0.  Exit")
            print("="*80)

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.start_server()
            elif choice == "2":
                self.analyze_project()
            elif choice == "3":
                self.seo_audit()
            elif choice == "4":
                self.create_backup()
            elif choice == "5":
                self.list_all_files()
            elif choice == "6":
                self.update_version()
            elif choice == "7":
                self.setup_project_structure()
            elif choice == "8":
                print(json.dumps(self.config, indent=4))
            elif choice == "0":
                print("👋 Thank you for using Apple Dev Tools!")
                break
            else:
                print("❌ Invalid option. Please try again.")

    def setup_project_structure(self):
        folders = ["assets/images/products", "assets/icons", "assets/css", "assets/js"]
        for folder in folders:
            (self.root / folder).mkdir(parents=True, exist_ok=True)
            print(f"✅ Folder created: {folder}")


# ====================== ENTRY POINT ======================
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "server":
        AppleDevTools().start_server()
    else:
        tools = AppleDevTools()
        tools.show_menu()
