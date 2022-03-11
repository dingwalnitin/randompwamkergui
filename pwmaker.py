import random
import tkinter as tk
import os
import sys
import pyperclip
def PwMaker():
    PTem= []
    nu=random.randint(7,15)
    for i in range (nu):
        charnum=int(random.randint(33,125))
        disp=chr(charnum)
        PTem.append(disp)
    z = "".join(PTem)
    return z

m=PwMaker()
root= tk.Tk()
root.title("random pw genrator by nitin")
root.geometry('600x500')
def restart_program():

    python = sys.executable
    os.execl(python, python, * sys.argv)

def cop():
    pyperclip.copy(m)

l = tk.Label(root, text = "program by nitin")
l.config(font =("Courier", 14))
l.pack()

T = tk.Text(root, height = 2, width = 30)
T.pack()
T.insert(tk.END, m)

tk.Button(root, text="Copy to clipboard", command=cop).pack()
tk.Button(root, text="Restart", command=restart_program).pack()

root.mainloop()







