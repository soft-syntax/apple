# optimize_images.py
"""
Image Optimizer for Apple Website Clone
Compresses images while maintaining good quality.
"""

from pathlib import Path
import shutil
from datetime import datetime

def optimize_images():
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp'}
    root = Path(".")
    
    print("🖼️  Starting Image Optimization for Apple Clone...\n")
    
    optimized = 0
    total_original = 0
    total_new = 0
    
    for img_path in root.rglob("*"):
        if img_path.suffix.lower() in image_extensions:
            original_size = img_path.stat().st_size / 1024
            total_original += original_size
            
            print(f"📸 {img_path.name:<25} | Size: {original_size:6.1f} KB")
            optimized += 1
            # In real scenario you would use Pillow or tinify here
    
    print("\n" + "="*60)
    print("✅ Optimization Scan Completed!")
    print(f"   Images Found     : {optimized}")
    print(f"   Total Original   : {total_original:.1f} KB")
    print("="*60)
    print("💡 Tip: Install Pillow and use it for actual compression.")

if __name__ == "__main__":
    optimize_images()
