import os
import shutil



source_dir = "/Users/tanishkamath/Downloads"

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", "DNG"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}

def organize_files (directory):

    for filename in os.listdir(directory):

        if os.path.isdir(os.path.join(directory, filename)):
            continue

        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        category = "others"
        for cat, extensions in CATEGORIES.items():
            
            if file_extension in extensions :
                category = cat
                break

        category_folder = os.path.join(directory, category)

        if not os.path.exists(category_folder):

            os.makedirs(category_folder)

        shutil.move(
            os.path.join(directory, filename),
            os.path.join(category_folder, filename))

        print(f"Moved: {filename} -> {category}")

def main():
   
    directory = source_dir

    
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    
    organize_files(directory)
    print("File organization complete!")


if __name__ == "__main__":
    main()

    