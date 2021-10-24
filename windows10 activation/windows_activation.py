"""windows actvation pakages"""
import threading
from tkinter import ttk
import os
import tkinter
from PIL import ImageTk, Image


def unlock():
    """allows threading that helps with perforamnce"""
    pb.place(x=10, y=170)
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
    pb['value'] += 20
    os.system("slmgr.vbs /ato")


if __name__ == "__main__":

    root = tkinter.Tk()
    root.config(bg="#218DBF")
    root.title("Windows Activation")

    try:root.iconbitmap('./icon.ico')
    except:pass

    root.geometry("300x230")
    root.minsize(300, 230)
    root.maxsize(300, 230)

    try:

        image1 = Image.open("icon.ico")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=test, bg="#218DBF")
        label1.image = test
        label1.place(x=70, y=1)
    except:pass

    lab = tkinter.Label(root, text="! make sure you open this software as admin", bg="lightblue")
    lab.place(y=120, x=10)

    pb = ttk.Progressbar(root, orient='horizontal',mode='determinate', length=280)
 

    B = tkinter.Button(root, text="Activate", command=unlock)
    B.place(x=100, y=200)

    root.mainloop()
