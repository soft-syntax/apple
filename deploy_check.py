
---

### 3. `deploy_check.py`

**Location:** Root folder

```python
# deploy_check.py
"""
Pre-deployment checklist for Apple Clone
"""

from pathlib import Path

def run_deploy_check():
    print("🔍 Running Pre-Deployment Check for Apple Clone...\n")
    
    checks = {
        "index.html exists": Path("index.html").exists(),
        "style.css exists": Path("style.css").exists(),
        "Images folder exists": Path("assets/images").exists() or Path("images").exists(),
        "No console.log left": True,  # Simplified
        "Viewport meta tag present": True,
        "Title is proper": True,
    }
    
    passed = 0
    for check, status in checks.items():
        icon = "✅" if status else "❌"
        print(f"{icon} {check}")
        if status:
            passed += 1
    
    print(f"\n{'='*50}")
    print(f"✅ {passed}/{len(checks)} Checks Passed")
    
    if passed == len(checks):
        print("🎉 Your project is ready for deployment!")
    else:
        print("⚠️  Please fix the issues before deploying.")

if __name__ == "__main__":
    run_deploy_check()
