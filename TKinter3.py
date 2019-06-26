from tkinter import *

root = Tk()

photo = PhotoImage(file='18.gif')
theLable = Label(root,
                 text='学习python\n到哔哩哔哩',
                 justify=LEFT,
                 image = photo,
                 compound=CENTER,
                 font=("华康少女字体",20),
                 fg = "purple")
theLable.pack()
mainloop()