import os
import shutil

source_dir = r"C:\Users\michael\Downloads"  # Ensure this is a raw string with 'r'

# Create dictionary of folders
folders = {
    "ZIP": os.path.join(source_dir, "ZIP"),
    "images": os.path.join(source_dir, "images"),
    "videos": os.path.join(source_dir, "videos"),
    "Applications": os.path.join(source_dir, "Applications"),
    "PDF": os.path.join(source_dir, "PDF"),
    "documents": os.path.join(source_dir, "documents"),
    "installs": os.path.join(source_dir, "installs"),
    "others": os.path.join(source_dir, "others")
}

# Create folders if they don't exist
for folder_path in folders.values():
    os.makedirs(folder_path, exist_ok=True)

# Move files
def automation():
    for file in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, file)):
            if file.endswith(".zip"):
                print(f"Moving {file} to ZIP folder.")
                shutil.move(os.path.join(source_dir, file), folders["ZIP"])
            elif file.endswith((".png", ".jpg", ".jpeg")): 
                print(f"Moving {file} to images folder.")
                shutil.move(os.path.join(source_dir, file), folders["images"])
            elif file.endswith(".mp4"):
                print(f"Moving {file} to videos folder.")
                shutil.move(os.path.join(source_dir, file), folders["videos"])    
            elif file.endswith(".exe"):
                print(f"Moving {file} to Applications folder.")
                shutil.move(os.path.join(source_dir, file), folders["Applications"])
            elif file.endswith(".pdf"):
                print(f"Moving {file} to PDF folder.")
                shutil.move(os.path.join(source_dir, file), folders["PDF"])
            elif file.endswith((".doc", ".docx", ".txt")):
                print(f"Moving {file} to documents folder.")
                shutil.move(os.path.join(source_dir, file), folders["documents"])
            elif file.endswith((".msi",".iso")):
                print(f"Moving {file} to installs folder.")
                shutil.move(os.path.join(source_dir, file), folders["installs"])
            else:
                print(f"Moving {file} to others folder.")
                shutil.move(os.path.join(source_dir, file), folders["others"])

automation()
