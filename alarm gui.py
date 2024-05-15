from tkinter import *
from PIL import Image, ImageTk
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from pygame import mixer
import re
def snooze():
        import time
        t = int(input("enter snooze time[10,20,30]"))
        if t == 10:
            time.sleep(10)
        elif t == 20:
            time.sleep(20)
        else:
            time.sleep(30)
        mixer.init()
        mixer.music.load("eyes.mp3")
        mixer.music.play()

def alarm():
            import tkinter.messagebox as t
            mixer.init()
            mixer.music.load("eyes.mp3")
            mixer.music.play()
            a=t.askquestion("dismiss","do u want to dismiss click yes or to snooze click no")
            print(a)
            if a=="yes":
                mixer.music.stop()
            else:
                mixer.music.stop()
                import time
                time.sleep(10)
                mixer.init()
                mixer.music.load("eyes.mp3")
                mixer.music.play()
                a = t.askquestion("dismiss", "do u want to cancel")
                print(a)
                if a == "yes":
                    mixer.music.stop()



def select():
    value = str((b.get(ACTIVE)))
    value1 = str((b1.get(ACTIVE)))
    value2 = str((b3.get(ACTIVE)))
    wanted_time = value+":"+value1 + " " +value2
    #print(wanted_time)
    wanted_time1 = value + ":" + value1
    while True:
        #global wanted_time
        time1=wanted_time1
        query = wanted_time
        if "p.m" in query and int(time1.split(":")[0]) < 12:
            ti = int(time1.split(":")[0]) + 12
            tim = str(ti)
            time2 = tim + ":" + time1.split(":")[1] + ":00"
            print(time2)
            twe = time2.split(":")[0]
        elif "p.m" in query and int(time1.split(":")[0]) == 12:
            ti1 = int(time1.split(":")[0])
            time2 =str(ti1) + ":" + (time1.split(":")[1]) + ":00"
            print(time2)
        else:
            if int(time1.split(":")[0]) < 10:
                time2 = "0" + time1 + ":00"
                print(time2)
            elif int(time1.split(":")[0])==12:
                ti1=int(time1.split(":")[0])-12
                time2="0"+str(ti1)+":"+(time1.split(":")[1])+":00"
                print(time2)
            else:
                time2 = time1 + ":00"
                print(time2)


        while True:

            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            print(time2)
            if time2 == time:
                alarm()
                break




root=Tk()
root.geometry("600x400")
root.maxsize(600,275)
root.minsize(600,275)
root.title("ALARM")
image=Image.open("clock2.png")
photo1=ImageTk.PhotoImage(image)
root.wm_iconphoto(False,photo1)
a=Label(root,image=photo1)
a.place(x=0,y=0)
f1=Frame(root,bg="black")
f1.place(x=200,y=120)
f2=Frame(root,bg="black")
f2.place(x=350,y=120)
scroll=Scrollbar(f1)
scroll.pack(side=RIGHT,fill=Y)
b=Listbox(f1,width=2,height=1,yscrollcommand=scroll.set,font="comisansms 32 bold")
b.pack(pady=10,padx=10)
for i in range(1,13):
    b.insert(END,i)
scroll.config(command=b.yview)
scroll1=Scrollbar(f2)
scroll1.pack(side=RIGHT,fill=Y)
b1=Listbox(f2,width=2,height=1,yscrollcommand=scroll1.set,font="comisansms 32 bold")
b1.pack(pady=10,padx=10)
for i in range(0,60):
    if i<=9:
        b1.insert(END,f"0{i}")
    else:

        b1.insert(END,i)
scroll1.config(command=b1.yview)

f3=Frame(root,bg="black")
f3.place(x=450,y=125)
scroll3=Scrollbar(f3)
scroll3.pack(side=RIGHT,fill=Y)
b3=Listbox(f3,width=4,height=1,yscrollcommand=scroll3.set,font="comisansms 22 bold")
b3.pack(pady=10,padx=10)
b3.insert(ACTIVE,"a.m")
b3.insert(ACTIVE,"p.m")
scroll3.config(command=b3.yview)
but=Button(root,text='SET',bg="white",padx=14,command=select)
but.pack()
but.place(x=50,y=90)

# but=Button(root,text='SNOOZE',bg="white",command=stop)
# but.place(x=50,y=190)
label=Label(text="ALARM",fg="white",bg="black",font="72")
label.place(x=250,y=45)
root.mainloop()