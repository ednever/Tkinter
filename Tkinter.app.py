from tkinter import *
aken = Tk()
aken.title("Menu")
aken.geometry("800x500")
k=0
def klikker(event):
    global k
    k += 1
    nupp.config(text = k)

def klikker2(event):
    global k
    k -= 1
    nupp.config(text = k)

def txt_to_lbl(event):
    t = txt.get()
    lbl.configure(text = t)
    txt.delete(0,END)

def valimine():
    valik = var.get()
    lbl.configure(text = valik)
    txt.insert(0,valik)

nupp = Button(aken,text = "Mina olen nupp",font = "Arial20", width = 20,bg = "red",fg = "green",relief = RAISED)
nupp.pack()#place(x = 400,y = 250)#side = LEFT
nupp.bind("<Button-1>",klikker)
nupp.bind("<Button-3>",klikker2)

lbl = Label(aken,text = "...",height = 3,width = 20,font = "Arial20",fg = "green",bg = "yellow",relief = "solid")
lbl.pack()

txt = Entry(aken,width = 20,font = "Arial20",fg = "green",bg = "lightblue",justify = CENTER)
txt.pack()
txt.bind("<Return>",txt_to_lbl)#Enter

i1 = PhotoImage(file = "1.gif")
i2 = PhotoImage(file = "2.gif")
i3 = PhotoImage(file = "3.gif")

var = StringVar()
var.set("Üks")
r1 = Radiobutton(aken,image = i1,variable = var,value = "Üks",command = valimine)
r2 = Radiobutton(aken,image = i2,variable = var,value = "Kaks",command = valimine)
r3 = Radiobutton(aken,image = i3,variable = var,value = "Kolm",command = valimine)
r1.pack(side = LEFT)
r2.pack(side = LEFT)
r3.pack(side = BOTTOM)

aken.mainloop()