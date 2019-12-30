from Tkinter import *
import os

root=Tk()

root.title("Cpcp APP")

def fun():
    os.system("python3 cpp.py "+coi.get())

e1=Label(root,text="Enter the Cont ID")
e1.pack()

coi=Entry(root)
coi.pack()

but=Button(root,text="Fetch it",command=fun)
but.pack()
root.mainloop()
