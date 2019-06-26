from tkinter import *

def callback():
    var.set("吹吧你，我才不信！")
root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('您所下载的影片含有未成年人限制内容\n请满18周岁后观看')
textLable = Label(frame1,
                  textvariable=var,
                  justify=LEFT,
                  padx=10)
textLable.pack(side=LEFT)

photo = PhotoImage(file='18.gif')
imgLable = Label(frame1,image=photo)
imgLable.pack(side = RIGHT)

theBurron = Button(frame2,text='我已满18岁',command=callback)
theBurron.pack()

frame1.pack( padx=10,pady=10)
frame2.pack()
mainloop()