import os
import shutil

# ==================== تنظیمات ====================
# پوشه‌ای که می‌خوای مرتب کنی (مسیر خودت رو بذار)
TARGET_FOLDER = "C:/Users/HP ZBOOK 15 G8/Downloads"

# دسته‌بندی بر اساس پسوند فایل
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".apk"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}


def get_category(filename):
    """تشخیص دسته‌ی فایل بر اساس پسوند"""
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def organize_folder(folder_path):
    """مرتب کردن فایل‌های یه پوشه"""
    if not os.path.exists(folder_path):
        print(f"❌ پوشه پیدا نشد: {folder_path}")
        return

    moved_count = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # اگه پوشه بود، رد کن
        if os.path.isdir(file_path):
            continue

        # تشخیص دسته
        category = get_category(filename)

        # ساخت پوشه‌ی دسته (اگه نبود)
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

        # انتقال فایل
        new_path = os.path.join(category_folder, filename)

        # اگه فایل هم‌نام وجود داشت، اسم رو عوض کن
        if os.path.exists(new_path):
            name, ext = os.path.splitext(filename)
            new_path = os.path.join(category_folder, f"{name}_copy{ext}")

        shutil.move(file_path, new_path)
        print(f"✅ {filename} → {category}/")
        moved_count += 1

    print(f"\n🎉 {moved_count} فایل مرتب شد!")


def main():
    print("📂 مرتب‌کننده‌ی خودکار فایل‌ها")
    print(f"🎯 پوشه‌ی هدف: {TARGET_FOLDER}\n")

    confirm = input("ادامه می‌دی؟ (y/n): ").strip().lower()
    if confirm != "y":
        print("لغو شد.")
        return

    organize_folder(TARGET_FOLDER)


if __name__ == "__main__":
    main()