# File organizer

<!-- VS Code -->
<img src="https://code.visualstudio.com/assets/images/code-stable.png" alt="VS Code Logo" width="50">   



An easy to use python script that allows you to organize your files in any directory on your laptop. 

## Installation instruction

First clone the directory in your terminal
```bash
git clone https://github.com/Tanish719/FIle_organizer.git
```

Then switch directories into the main folder using ```cd File_organizer/Main_code```. 

After that you can access the main python file organizer.py.

## How to use

By defaul the file organizer targety your downloads folder and organizes filetypes in categories as shown below.
```python
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", "DNG"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}
```

You can paste the path to the directory directiy into the terminal
```bash
Enter path: Users/username/path
```
Additionally for those who prefer a fixed input you can paste the directory path of the folder you want the files to be organized direclty into the source_dir variable. 
```python
source_dir = "Paste your path here"
```
You can now view a summary of what has been moved where in the summary_report.txt file that gets newly created and replaced everytime you run the script to give you an overview of the moved files. Furthermore, there is also a .log file to see the log of the terminal
