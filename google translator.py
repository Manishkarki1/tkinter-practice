from tkinter import ttk
from tkinter import *
from googletrans import Translator,LANGUAGES

def conversion(text="type",src="English",dest="Nepali"):
    # text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1

def data():
    s=combo_sour.get()
    d=combo_desti.get()
    msg=sour_txt.get(1.0,END)
    textget=conversion(text=msg,src=s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root=Tk()
root.title("Translator")
root.config(bg="blue")
root.iconbitmap("")

label1=Label(root,text="Translator",font=("Time New Roman",30,"bold"),bg="white")
label1.pack()

frame=Frame(root).pack(side=BOTTOM)

label2=Label(root,text="Source Text",font=("Time New Roman",30,"bold"),fg="red",pady=30,bg="white")
# label2.place(x=100,y=100,height=20,width=300)
label2.pack(pady=5)

sour_txt=Text(frame,font=("Time New Roman",20,"italic"),wrap=WORD,height=3,width=90)
# sour_txt.place(x=10,y=130,height=150,width=480)
sour_txt.pack(pady=5)

list_text=list(LANGUAGES.values())

combo_sour= ttk.Combobox(frame,values=list_text)
combo_sour.place(x=10,y=300,height=40,width=150)
combo_sour.set("english")

translatebtn=Button(frame,text="Translate",relief=RAISED,command=data)
translatebtn.place(x=170,y=300,height=40,width=150)

combo_desti=ttk.Combobox(frame,values=list_text)
combo_desti.place(x=330,y=300,height=40,width=150)
combo_desti.set("english")

label3=Label(root,text="Destination Text",font=("Time New Roman",30,"bold"),fg="red",bg="white")
label3.place(x=520,y=360,height=50,width=300)

dest_txt=Text(frame,font=("Time New Roman",20,"italic"),wrap=WORD,height=3,width=90)
dest_txt.place(x=10,y=420)

root.mainloop()