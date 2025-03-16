import os
import shutil
import logging
from collections import defaultdict

from datetime import datetime

# Configure logging
log_file = "moved_files.log"
logging.basicConfig(
    filename=log_file, 
    level=logging.INFO, 
    format="%(asctime)s - %(message)s",
    filemode="a"  
)

source_dir = input("Enter path: ")

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", "DNG"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}

def organize_files(directory):
    file_counts = defaultdict(int)  # Track count of files per category
    
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            continue
        
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        category = "Others"

        for cat, extensions in CATEGORIES.items():
            if file_extension in extensions:

                category = cat
                break

        category_folder = os.path.join(directory, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        
        new_path = os.path.join(category_folder, filename)
        shutil.move(os.path.join(directory, filename), new_path)
        
        logging.info(f"Moved: {filename} -> {category}")
        file_counts[category] += 1
        
        print(f"Moved: {filename} -> {category}")
    
    generate_report(file_counts)
    



def generate_report(file_counts):

    report_file = "summary_report.txt"

    with open(report_file, "w") as f:
        
        f.write("File Organization Summary\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for category, count in file_counts.items():
            f.write(f"{category}: {count} files moved\n")

    print("Summary report generated! Check summary_report.txt")

def main():
    if not os.path.exists(source_dir):

        print("Directory does not exist!")
        return
    
    organize_files(source_dir)
    print("File organization complete!")

if __name__ == "__main__":
    main()
