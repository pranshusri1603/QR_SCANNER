from tkinter import *
import qrcode

win=Tk()
win.title('QrCode Generator')
win.geometry('1366x768+0+0')
win.configure(bg='#AE2321')
win.resizable(False,False)

def generate():
    name=title.get()
    text=ent.get()
    qr=qrcode.make(text)
    qr.save('qrcode/'+str(name)+'.png')

Label(win,text='Title',fg='white',bg='#AE2321',font='Arial 15').place(x=50,y=170)
title=Entry(win,width=13,font='Arial 15')
title.place(x=50,y=200)

ent=Entry(win,width=27,font='Arial 15')
ent.place(x=50,y=250)

Button(win,text='Generator',bg='Black',fg='white',command=generate).place(x=50,y=300)
win.mainloop()          
                                                         
      
