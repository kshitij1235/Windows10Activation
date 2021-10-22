"""windows actvation pakages"""
import threading
from tkinter import ttk
import os
import tkinter
from PIL import ImageTk, Image


def unlock():
    """allows threading that helps with perforamnce"""
    threading.Thread(target=commands).start()


def commands():
    """commands that help windows activation"""
    pb['value'] += 20
    os.system("c:")
    pb['value'] += 10
    os.system("cd C:/WINDOWS/system32")
    pb['value'] += 30
    os.system("slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    pb['value'] += 10
    os.system("slmgr.vbs /skms kms.lotro.cc")
    pb['value'] += 10
    os.system("slmgr.vbs /ato")
    pb['value'] += 20


if __name__ == "__main__":

    # gui code

    # root window
    root = tkinter.Tk()
    root.config(bg="#218DBF")
    # TITLE
    root.title("Windows Activation")
    try:
        root.iconbitmap('./icon.ico')
    except:
        pass

    # SCREENSIZE
    root.geometry("300x230")
    root.minsize(300, 230)
    root.maxsize(300, 230)

    # menu widigits
    try:

        image1 = Image.open("icon.ico")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test, bg="#218DBF")
        label1.image = test
        # Position image
        label1.place(x=70, y=1)
    except:
        pass

    lab = tkinter.Label(
        root, text="! make sure you open this software as admin", bg="lightblue")
    lab.place(y=120, x=10)

    pb = ttk.Progressbar(root, orient='horizontal',
                         mode='determinate', length=280)
    pb.place(x=10, y=170)

    B = tkinter.Button(root, text="Activate", command=unlock)
    B.place(x=100, y=200)

    root.mainloop()
