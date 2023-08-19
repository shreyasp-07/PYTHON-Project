from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="english", dest="hindi"):
    text1=text
    src1=src
    dest1=dest
    print(text1,src1,dest1)
    trans = Translator()
    trans1 = trans.translate(text1,src=src1,dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0, END)
    textget = change(text=msg,src=s,dest=d)
    Dest_txt.delete(1.0,END)
    Dest_txt.insert(END,textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Red')

lab_txt=Label(root, text="Translator", font=("Time New Roman",45,"bold"), bg="Red", fg="White")
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root, text="Enter Text", font=("Time New Roman",20,"bold"), bg="Red", fg="White")
lab_txt.place(x=100, y=110, height=20, width=300)

Sor_txt = Text(frame, font=("Time New Roman",45,"bold"), wrap=WORD)
Sor_txt.place(x=10,y=140,height=150,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=10, y=310, height=40, width=150)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=180, y=310, height=40, width=140)

comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=340, y=310, height=40, width=150)
comb_dest.set("english")

lab_txt=Label(root, text="Translated Text", font=("Time New Roman",20,"bold"), bg="Red", fg="White")
lab_txt.place(x=100, y=370, height=20, width=300)

Dest_txt = Text(frame, font=("Time New Roman",45,"bold"), wrap=WORD)
Dest_txt.place(x=10,y=410,height=150,width=480)

root.mainloop()