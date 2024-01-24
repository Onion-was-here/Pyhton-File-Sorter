import os
import shutil
import tkinter as tk
from tkinter import filedialog
import PIL


def set_path():
    global path
    path = filedialog.askdirectory()

    if os.path.exists(path):
        extension(path)
    else:
        print("File path does not exist")


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


root = tk.Tk()

root['bg'] = 'white'
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = int(screen_width/2)
window_height = int(screen_height/8)
window_size = str(window_width)+'x'+str(window_height)
root.geometry(window_size)

input_frame = tk.Frame(master=root)
entry_frame = tk.Frame(master=input_frame)

button = tk.Button(master=root, text='Enter Directory',
                   command=set_path, anchor='center')
img = tk.PhotoImage(file="C:/coding proj/Better File sorter/button.png")
button.config(image=img)
button["bg"] = "white"
button["border"] = "0"
button.pack(pady=20)


root.mainloop()
