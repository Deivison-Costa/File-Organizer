import os
import shutil

def organize_files(folder_path):
    # Extensões dos arquivos e os nomes de pastas correspondentes
    file_types = {
        ".txt": "Text Files",
        ".docx": "Word Documents",
        ".pdf": "PDFs",
        ".jpg": "Images",
        ".png": "Images",
        ".xlsx": "Excel Files",
        ".mp3": "Music",
        ".mp4": "Videos",
        ".zip": "Compressed Files",
        ".rar": "Compressed Files",
        ".gz": "Compressed Files",
        ".tar": "Compressed Files",
        ".7z": "Compressed Files",
        ".pptx": "PowerPoint Presentations",
        ".csv": "CSV Files",
    }

    # Criando subpastas para cada tipo de arquivo
    for folder_name in file_types.values():
        folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Organizando os arquivos com base em seus tipos
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            if ext in file_types:
                destination_folder = os.path.join(folder_path, file_types[ext])
                shutil.move(file_path, destination_folder)

    print("Files organized successfully.")

def remove_empty_folders(folder_path):
    for root, dirs, _ in os.walk(folder_path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

    print("Empty folders removed successfully.")

def main():
    folder_path = input("Enter the path to the folder you want to organize: ")
    organize_files(folder_path)
    remove_empty_folders(folder_path)

if __name__ == "__main__":
    main()
