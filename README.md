# File organizer

An easy to use python script that allows you to organize your files in any directory on your laptop. 

## Installation instruction

First clone the directory in your terminal
```bash
git clone https://github.com/Tanish719/FIle_organizer.git
```

Then switch directories into the main folder using ```cd File_organizer/Main_code```. 

After that you can access the main python file.

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

You can add or remove categories to your liking. To change the directory in which the scipt organzies your files simply paste your code into the **source_dir** variable.
```python
source_dir = "/Users/User_name/Downloads"
```
Additionally for those who prefer a user input you can paste this code instead of the one above. 
```python
source_dir = input("Enter directory_path: ")
```
Then you can copy the directory path of whatever folder you want from your files app and paste it into the terminal when you run the script. 