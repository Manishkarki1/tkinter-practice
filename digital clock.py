from tkinter import *
import datetime

clock=Tk()
clock.title("Digital Clock")
clock.config(bg="green")
clock.geometry("1000x500")

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime("%I")
    min=time.strftime("%M")
    sec=time.strftime("%S")
    am=time.strftime("%p")
    date=time.strftime("%d")
    mon=time.strftime("%m")
    year=time.strftime("%y")
    day=time.strftime("%a")

    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_ap.config(text=am)
    lab_date.config(text=date)
    lab_month.config(text=mon)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(200,date_time)

label1=Label(clock,text="***Digital clock***",fg="white",bg="green",font=("Time New Roman",50,"bold"))
label1.pack()
# time
lab_hr=Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_hr.place(x=200,y=100,height=100,width=100)
txt_hr=Label(clock,text="Hour",font=("Time New Roman",20,"italic"),fg="black",bg="green")
txt_hr.place(x=220,y=200)

lab_min=Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_min.place(x=400,y=100,height=100,width=100)
txt_min=Label(clock,text="Minute",font=("Time New Roman",20,"italic"),fg="black",bg="green")
txt_min.place(x=400,y=200)

lab_sec=Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_sec.place(x=600,y=100,height=100,width=100)
txt_sec=Label(clock,text="Second",font=("Time New Roman",20,"italic"),fg="black",bg="green")
txt_sec.place(x=600,y=200)

lab_ap=Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_ap.place(x=800,y=100,height=100,width=100)
txt_ap=Label(clock,text="AM/PM",font=("Time New Roman",20,"italic"),fg="black",bg="green")
txt_ap.place(x=800,y=200)

#Date
lab_date=Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_date.place(x=200,y=300,height=100,width=100)
txt_date=Label(clock,text="Date",font=("Time New Roman",20,"italic"),fg="black",bg="green")
txt_date.place(x=220,y=400)

lab_month=Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_month.place(x=400,y=300,height=100,width=100)
txt_month=Label(clock,text="Month",font=("Time New Roman",20,"italic"),fg="black",bg="green")
txt_month.place(x=400,y=400)

lab_year=Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_year.place(x=600,y=300,height=100,width=100)
txt_year=Label(clock,text="Year",font=("Time New Roman",20,"italic"),fg="black",bg="green")
txt_year.place(x=620,y=400)

lab_day=Label(clock,text="00",font=("Time New Roman",40,"bold"),bg="red",fg="white")
lab_day.place(x=800,y=300,height=100,width=100)
txt_day=Label(clock,text="Day",font=("Time New Roman",20,"italic"),fg="black",bg="green")
txt_day.place(x=820,y=400)

date_time()
clock.mainloop()
