import sys
if sys.version_info[0] == 3:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
else:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter
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
