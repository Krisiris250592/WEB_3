import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def process_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        _, file_extension = os.path.splitext(file)
        destination_folder = os.path.join(folder_path, file_extension[1:])

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        source_path = os.path.join(folder_path, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)

def process_subfolder(subfolder_path):
    for root, dirs, files in os.walk(subfolder_path):
        for file in files:
            file_path = os.path.join(root, file)
            process_folder(file_path)

def process_main_folder(root_folder):
    subfolders = [os.path.join(root_folder, d) for d in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, d))]


    with ThreadPoolExecutor() as executor:
        executor.map(process_subfolder, subfolders)

if __name__ == "__main__":
    folder_path = r"C:\Users\Kristina Cherchataya\хлам"
    process_main_folder(folder_path)