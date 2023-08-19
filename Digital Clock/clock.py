from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")
    
    
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_ampm.config(text=am)
    lab_dt.config(text=date)
    lab_mnth.config(text=month)
    lab_yr.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(200, date_time)

clock = Tk()
clock.title("Digigtal Clock")
clock.geometry('1000x550')
clock.config(bg='yellow')

lab_hr = Label(clock, text='00', font=('Time New Roman', 60, "bold"),
               bg='red',fg="white")
lab_hr.place(x=110, y=40, height=110, width=110)

lab_min = Label(clock, text='00', font=('Time New Roman', 60, "bold"),
               bg='red',fg="white")
lab_min.place(x=330, y=40, height=110, width=110)

lab_sec = Label(clock, text='00', font=('Time New Roman', 60, "bold"),
               bg='red',fg="white")
lab_sec.place(x=550, y=40, height=110, width=110)

lab_ampm = Label(clock, text='00', font=('Time New Roman', 50, "bold"),
               bg='red',fg="white")
lab_ampm.place(x=770, y=40, height=110, width=110)


lab_hrt = Label(clock, text='Hour', font=('Time New Roman', 30, "bold"),
               bg='red',fg="white")
lab_hrt.place(x=110, y=180, height=60, width=110)

lab_mint = Label(clock, text='Min', font=('Time New Roman', 30, "bold"),
               bg='red',fg="white")
lab_mint.place(x=330, y=180, height=60, width=110)

lab_sect = Label(clock, text='Sec', font=('Time New Roman', 30, "bold"),
               bg='red',fg="white")
lab_sect.place(x=550, y=180, height=60, width=110)

lab_ampmt = Label(clock, text='AM/PM', font=('Time New Roman', 20, "bold"),
               bg='red',fg="white")
lab_ampmt.place(x=770, y=180, height=60, width=110)


lab_dt = Label(clock, text='00', font=('Time New Roman', 60, "bold"),
               bg='red',fg="white")
lab_dt.place(x=110, y=290, height=110, width=110)

lab_mnth = Label(clock, text='00', font=('Time New Roman', 60, "bold"),
               bg='red',fg="white")
lab_mnth.place(x=330, y=290, height=110, width=110)

lab_yr = Label(clock, text='00', font=('Time New Roman', 60, "bold"),
               bg='red',fg="white")
lab_yr.place(x=550, y=290, height=110, width=110)

lab_day = Label(clock, text='Day', font=('Time New Roman', 40, "bold"),
               bg='red',fg="white")
lab_day.place(x=770, y=290, height=110, width=110)


lab_dtt = Label(clock, text='Date', font=('Time New Roman', 30, "bold"),
               bg='red',fg="white")
lab_dtt.place(x=110, y=430, height=60, width=110)

lab_mntht = Label(clock, text='Month', font=('Time New Roman', 25, "bold"),
               bg='red',fg="white")
lab_mntht.place(x=330, y=430, height=60, width=110)

lab_yrt = Label(clock, text='Year', font=('Time New Roman', 30, "bold"),
               bg='red',fg="white")
lab_yrt.place(x=550, y=430, height=60, width=110)

lab_dayt = Label(clock, text='Day', font=('Time New Roman', 30, "bold"),
               bg='red',fg="white")
lab_dayt.place(x=770, y=430, height=60, width=110)

date_time()

clock.mainloop()