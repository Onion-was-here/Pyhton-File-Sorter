import os
import shutil

path = r"C:\Users\Orion\Desktop\New folder"


def extension(path):
    Files = os.listdir(path)
    # extension_list = list(set(Files.split('.')[-1]))

    # extension list is also the list and name of folders
    # because the naming convention of thiis ccode is such that
    # all organised files are sorted based on the extension

    for e in Files:
        if os.path.isfile(os.path.join(path, e)):
            f_ext = e.split('.')[-1]
            folder_path = os.path.join(path, f_ext)

            if os.path.isdir(folder_path):
                shutil.move(os.path.join(path, e),
                            os.path.join(folder_path, e))
            else:
                os.makedirs(folder_path)
                shutil.move(os.path.join(path, e),
                            os.path.join(folder_path, e))


if __name__ == "__main__":
    extension(path)
