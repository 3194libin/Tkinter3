from tkinter import *

root = Tk()

textLable = Label(root,text = '您所下载的电影含有未成年人限制内容，请满18周岁后观看！')
textLable.pack()

photo  =  PhotoImage(file="18.jpg")
imgLable = Label(root,image=photo)
imgLable.pack()

mainloop()