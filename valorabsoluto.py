from tkinter import *
def valorabs():
    val1=abs(float(txt.get()))
    lbl1.configure(text="El valor absoluto es {0}".format(val1))


vtn=Tk()
vtn.title("Programa que calcula el valor absoluto")
vtn.iconbitmap("logo.ico")
vtn.geometry("300x200")
lbl=Label(vtn,text="Ingresa un numero")
lbl.grid(column=1,row=2,sticky=(W,E))
num=0
txt=Entry(vtn,width=10,textvariable=num)
txt.grid(column=2,row=2,sticky=(W,E))
btn=Button(vtn,text="Calcular",command=valorabs)
btn.grid(column=1,row=4,sticky=(W,E))
lbl1=Label(vtn,text="")
lbl1.grid(column=2,row=5,sticky=(W,E))
vtn.mainloop()