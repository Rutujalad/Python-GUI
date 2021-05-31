from tkinter import *
def resize():
    root.geometry(f"{widthvalue.get()}x{heightvalue.get()}")

root=Tk()
root.geometry("500x400")
root.title("Window Resizer")
Label(root,text="Enter the width of window:").grid(row=0,column=0)
Label(root,text=" Enter the Height of window:").grid(row=1,column=0)

widthvalue=IntVar()
heightvalue=IntVar()

widthEntry=Entry(root,textvariable=widthvalue).grid(row=0,column=1)
heightEntry=Entry(root,textvariable=heightvalue).grid(row=1,column=1)

Button(text="Resize", bg="black", fg="white", font="calibri 12 bold", command=resize).grid(row=5,column=0)

root.mainloop()