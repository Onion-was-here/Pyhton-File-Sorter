import shutil
import os
import tkinter as tk

path = r"C:\Users\Orion\Desktop\New folder"


extensions = {"Documents": ["doc", "docx", "txt", "pdf"],
              "Video": ["mkv", "mp4", "webm", "mov", "avi", "m4v"],
              "Audio": ["mp3", "wav", "flac"],
              "Images": ["psd", "jpg", "png", "tiff", "bmp"],
              "Zip": ["zip", "rar", "7z", "iso"],
              "Code": ["html", "css", "py", "js", "php", "rb", "xml", "json", "pyw", "c", "sh", "bat", "cs", "java"],
              "Other": []
              }


def sort(path, extensions):
    File_list = os.listdir(path)
    for e in File_list:
        if os.path.isfile(os.path.join(path, e)):
            f_ext = e.split('.')[-1]
            for folder, ext in extensions.items():
                if f_ext in ext:
                    org_folder_path = os.path.join(path, folder)
                    if not os.path.exists(org_folder_path):
                        os.makedirs(org_folder_path)
                        shutil.move(os.join(path, e),
                                    os.join(org_folder_path, e))
                    else:
                        folder_path = os.path.join(path, "Other")
                        os.makedirs(folder_path)
                        shutil.move(os.join(path, e), os.join(folder_path, e))


if __name__ == "__main__":
    sort(path, extensions)
