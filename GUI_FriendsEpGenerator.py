import random
from tkinter import *
root=Tk()
root.geometry("400x160")
root.title("Random Friends Episode Generator")
root.configure(bg='plum')
def friend1():
    a=[]
    for i in range(1,11):
        for j in range(1,26):
            a.append(f"Season {i} Episode {j}")
    b=random.choice(a)
    svvalue.set(b)
    screen.update()


Label(root,text="F•R•I•E•N•D•S",font="Helvetica 17 bold",bg="plum").pack(fill=X,pady=(5,0))
f1=Frame(root)
f1.pack(anchor="center")
svvalue=StringVar()
svvalue.set("")
screen=Entry(root,textvariable=svvalue,font="Arial 15 bold")
screen.pack(fill=X,ipady=13,pady=(5,0),padx=15)
b1=Button(root,bg="khaki",fg="black",font="Arial 12 bold",text="Random Friends Episode",command=friend1)
b1.pack(anchor="center",padx=15,pady=15,fill=X)

root.mainloop()