# File Organizer
- **file_organizer.py** is a Python script that helps you organize files in a specified folder based on their file types. It categorizes files into different subfolders, making it easier to manage and find files of specific types. 
- The script also includes a function to remove empty folders that may result from the organization process.

# Installation and Setup
- Clone the repository or download the source code.
- Make sure you have Python installed on your system (Python 3.x is recommended).

# Usage
## Run the imdb_analysis.py file to start the application:
    python file_organizer.py

- The script will prompt you to enter the path to the folder you want to organize. Provide the full path and press Enter.
- The script will organize the files in the specified folder into subfolders based on their file types. It will print "Files organized successfully." after completion.
- Additionally, the script will remove any empty folders that might have resulted from the organization process. It will print "Empty folders removed successfully."
# File Types and Corresponding Subfolders
## The script supports the following file types and organizes them into corresponding subfolders:

- .txt - Text Files
- .docx - Word Documents
- .pdf - PDFs
- .jpg - Images
- .png - Images
- .xlsx - Excel Files
- .mp3 - Music
- .mp4 - Videos
- .zip - Compressed Files
- .rar - Compressed Files
- .gz - Compressed Files
- .tar - Compressed Files
- .7z - Compressed Files
- .pptx - PowerPoint Presentations
- .csv - CSV Files

# Important Notes
- Make sure you have a backup of your files before running the script, especially if you're organizing files in important directories. Although the script is designed to move files to subfolders, it's always a good practice to have a backup.
- The script categorizes files based on their extensions. If you have files with custom extensions or extensions not listed in the script, they will not be moved to any subfolder.
