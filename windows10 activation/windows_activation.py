# pakages 

import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image  

import os 

def commands():
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
    root = tk.Tk()
    root.config(bg="#218DBF")
     #TITLE
    root.title("Windows Activation")
    try:
        root.iconbitmap('icon.ico')
    except:
        print("cant load icon")

    #SCREENSIZE
    root.geometry("300x230")
    root.minsize(300,230)
    root.maxsize(300,230)


    # menu widigits 

    image1 = Image.open("icon.ico")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image=test,bg="#218DBF")
    label1.image = test

    # Position image
    label1.place(x=70, y=1)


    lab=tk.Label(root,text="! make sure you open this software as admin",bg="lightblue")
    lab.place(y=120,x=10)

    pb = ttk.Progressbar(root,orient='horizontal',mode='determinate',length=280)
    pb.place(x=10,y=170)

    B = ttk.Button(root, text ="Activate",command=commands) 
    B.place(x=100, y=200)






    root.mainloop()