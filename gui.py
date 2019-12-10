from tkinter import *
from tkinter import ttk
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
root = Tk()
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New BibTeX library", command=donothing)
filemenu.add_command(label="Open library", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
rightframe = Frame(root)
rightframe.pack(pady=1)
middleframe = Frame(rightframe)
middleframe.pack(pady=1, padx=0)

new = PhotoImage(file='add-file.png')
newBtn = ttk.Button(middleframe, image=new, command="New BibTeX library")
newBtn.grid(row=0, column=0, padx=0)

open = PhotoImage(file='add.png')
openBtn = ttk.Button(middleframe, image=open, command="New BibTeX library")
openBtn.grid(row=0, column=1, padx=0)

save = PhotoImage(file='save.png')
saveBtn = ttk.Button(middleframe, image=save, command="Save")
saveBtn.grid(row=0, column=2, padx=0)

cut = PhotoImage(file='scissors.png')
cutBtn = ttk.Button(middleframe, image=cut, command="Cut")
cutBtn.grid(row=0, column=3, padx=0)

copy = PhotoImage(file='copy-content.png')
copyBtn = ttk.Button(middleframe, image=copy, command="Copy")
copyBtn.grid(row=0, column=4, padx=0)

paste = PhotoImage(file='clipboard-paste-button.png')
pasteBtn = ttk.Button(middleframe, image=paste, command="paste")
pasteBtn.grid(row=0, column=5, padx=0)

search = PhotoImage(file='magnifying-glass.png')
searchBtn = ttk.Button(middleframe, image=search, command="search")
searchBtn.grid(row=0, column=6, padx=0)

root.mainloop()