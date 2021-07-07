from tkinter import *
from tkinter.messagebox import showinfo
import os
from tkinter.filedialog import askopenfilename,asksaveasfilename

def NewFile():
    global file
    root.title("Untitled-Rutuja's Notepad")
    file = None
    textarea.delete(1.0, END)

def OpenFile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Document","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"-Rutuja's Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt" , filetypes=[("All Files", "*.*"), ("Text Document","*.txt")])
        if file == "":
            file = None
        else:
            f=open(file, "w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Rutuja's Notepad")
    else:
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

def ExitApp():
    root.destroy()

def Cut():
    textarea.event_generate(("<<Cut>>"))

def Copy():
    textarea.event_generate(("<<Copy>>"))

def Paste():
    textarea.event_generate(("<<Paste>>"))

def Aboutus():
    showinfo("About Us","This Notepad is made by Rutuja Lad.")

if __name__ == '__main__':
    root=Tk()
    root.geometry("600x500")
    root.title("Untitled-Rutuja's Notepad")


    textarea= Text(root,font="arial 12")
    file=None
    textarea.pack(expand=True, fill=BOTH)

    Menubar = Menu(root)

    filemenu=Menu(Menubar,tearoff=0)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open", command=OpenFile)
    filemenu.add_command(label="Save", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=ExitApp)
    Menubar.add_cascade(label="File", menu=filemenu)

    Editmenu = Menu(Menubar, tearoff=0)
    Editmenu.add_command(label="Cut", command=Cut)
    Editmenu.add_command(label="Copy", command=Copy)
    Editmenu.add_command(label="Paste", command=Paste)
    Menubar.add_cascade(label="Edit", menu=Editmenu)

    Helpmenu = Menu(Menubar, tearoff=0)
    Helpmenu.add_command(label="About Us", command=Aboutus)
    Menubar.add_cascade(label="Help", menu=Helpmenu)

    root.config(menu=Menubar)

    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand= scroll.set)

    root.mainloop()
