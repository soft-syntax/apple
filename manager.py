# ========================================================
# project_manager.py - Smart Project Manager for Apple Clone
# ========================================================

"""
Advanced Project Management Tool for your Apple Website Clone.
This is one of the most useful scripts you can have.
"""

from pathlib import Path
import os
import json
from datetime import datetime
import shutil

class AppleProjectManager:
    def __init__(self):
        self.root = Path(".")
        self.config_file = self.root / "project_config.json"

    def setup_project(self):
        """Initial project setup"""
        print("🍎 Setting up Apple Clone Project...\n")

        folders = ["assets/images", "assets/icons", "assets/videos", "backup"]
        for folder in folders:
            (self.root / folder).mkdir(parents=True, exist_ok=True)
            print(f"✅ Created folder: {folder}")

        self.create_default_config()
        print("\n🎉 Project setup completed successfully!")

    def create_default_config(self):
        config = {
            "project_name": "Apple Website Clone",
            "version": "1.0.0",
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "author": "soft-syntax",
            "features": [
                "Responsive Design",
                "Smooth Animations",
                "Sticky Navbar",
                "Product Showcase"
            ],
            "technologies": ["HTML5", "CSS3", "JavaScript"],
            "server_port": 8000
        }

        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
        
        print("✅ project_config.json created")

    def show_project_info(self):
        """Display project information"""
        print("="*65)
        print("🍎 APPLE WEBSITE CLONE - PROJECT INFO")
        print("="*65)

        if self.config_file.exists():
            with open(self.config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
            
            print(f"Project Name : {config['project_name']}")
            print(f"Version      : {config['version']}")
            print(f"Last Updated : {config['last_updated']}")
            print(f"Author       : {config['author']}")
            print(f"Server Port  : {config['server_port']}")
        else:
            print("No config file found. Run setup first.")

        # Show file count
        html = len(list(self.root.rglob("*.html")))
        css = len(list(self.root.rglob("*.css")))
        js = len(list(self.root.rglob("*.js")))
        
        print(f"\n📊 Files:")
        print(f"   HTML files : {html}")
        print(f"   CSS files  : {css}")
        print(f"   JS files   : {js}")

    def clean_project(self):
        """Clean unnecessary files"""
        print("🧹 Cleaning project...")

        patterns_to_remove = ["__pycache__", ".DS_Store", "*.log"]
        
        for pattern in patterns_to_remove:
            for file in self.root.rglob(pattern):
                try:
                    if file.is_file():
                        file.unlink()
                        print(f"🗑️  Deleted: {file}")
                    elif file.is_dir():
                        shutil.rmtree(file)
                        print(f"🗑️  Deleted folder: {file}")
                except:
                    pass

        print("✅ Project cleaned successfully!")

    def update_copyright(self):
        """Update copyright year in all HTML files"""
        year = datetime.now().year
        updated = 0

        for html_file in self.root.rglob("*.html"):
            try:
                content = html_file.read_text(encoding="utf-8")
                if "©" in content or "copyright" in content.lower():
                    new_content = content.replace(str(year-1), str(year))
                    html_file.write_text(new_content, encoding="utf-8")
                    updated += 1
            except:
                pass

        print(f"✅ Copyright year updated in {updated} files to {year}")

    def menu(self):
        while True:
            print("\n" + "="*60)
            print("🍎 Apple Clone Project Manager")
            print("="*60)
            print("1. Setup Project Structure")
            print("2. Show Project Info")
            print("3. Start Development Server")
            print("4. Clean Project")
            print("5. Update Copyright Year")
            print("6. Generate Project Report")
            print("0. Exit")
            print("="*60)

            choice = input("\nChoose an option: ").strip()

            if choice == "1":
                self.setup_project()
            elif choice == "2":
                self.show_project_info()
            elif choice == "3":
                os.system("python serve.py") if Path("serve.py").exists() else print("❌ serve.py not found")
            elif choice == "4":
                self.clean_project()
            elif choice == "5":
                self.update_copyright()
            elif choice == "6":
                self.show_project_info()
            elif choice == "0":
                print("👋 Thank you for using Apple Project Manager!")
                break
            else:
                print("Invalid option. Please try again.")


# Run the manager
if __name__ == "__main__":
    manager = AppleProjectManager()
    manager.menu()
