from tkinter import *
from PIL import Image,ImageTk
import qrcode
from qrcode import *
root=Tk()
root.title("QR Code Maker")
root.config(bg="blue")
# root.iconbitmap("")

label1=Label(root,text="Enter your Title")
label1.pack(pady=5)
title=Entry(root,width=50)
title.pack(padx=30,pady=10)
# title.insert(0,"Enter your title: ")

label2=Label(root,text="Enter URL").pack()
entry=Entry(root,width=50)
entry.pack(padx=30,pady=10)
# entry.insert(0,"Enter your Url: ")

def click():
    topic=title.get()
    Url=entry.get()
    img= qrcode.make(Url)
    img.save(r"C:\Users\ADMIN\Pictures\QR Code/"+str(topic)+".png")
    global img1
    img1=ImageTk.PhotoImage(Image.open(r"C:\Users\ADMIN\Pictures\QR Code/"+str(topic)+".png"))
    mylabel=Label(image=img1).pack(pady=20)


btn=Button(root,text="Generate QR Code",fg="white",bg="green",command=click).pack()

root.mainloop()


