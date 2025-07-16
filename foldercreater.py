import os
folder="new_folder"
if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Folder '{folder}' created successfully.")
else:
    print(f"Folder '{folder}' already exists.")