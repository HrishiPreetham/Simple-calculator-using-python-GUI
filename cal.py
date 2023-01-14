from tkinter import *
import math
root=Tk()
root.title('Scientific calculator')
e=Entry(root,width=35,borderwidth=5,font=("calibre",10,"bold"))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click(num):
    c=e.get()
    e.delete(0,END)
    e.insert(0,c+str(num))
    
def clear():
    e.delete(0,END)

def add():
    first=e.get()
    global fnum
    global calculation
    calculation="Addition"
    fnum=float(first)
    e.delete(0,END)

def subtraction():
    first=e.get()
    global fnum
    global calculation
    calculation="Subtraction"
    fnum=float(first)
    e.delete(0,END)

def multiply():
    first=e.get()
    global fnum
    global calculation
    calculation="Multiply"
    fnum=float(first)
    e.delete(0,END)

def divide():
    first=e.get()
    global fnum
    global calculation
    fnum=float(first)
    calculation="Divide"
    e.delete(0,END)

def square():
    first=e.get()
    global fnum
    global calculation
    fnum=float(first)
    calculation="square"
    e.delete(0,END)

def exponent():
    first=e.get()
    global fnum
    global calculation
    fnum=float(first)
    calculation="Exponent"
    e.delete(0,END)

def logarithm():
    first=e.get()
    global fnum
    global calculation
    fnum=int(first)
    calculation="Logarithm"

def sinangle():
    first=e.get()
    global fnum
    global calculation
    fnum=float(first)
    calculation="sin"
    e.delete(0,END)

def cosangle():
    first=e.get()
    global fnum
    global calculation
    fnum=float(first)
    calculation="cos"
    e.delete(0,END)

def tanangle():
    first=e.get()
    global fnum
    global calculation
    fnum=float(first)
    calculation="tan"
    e.delete(0,END)
def off():
    e.delete(0,END)
    
    
    
def equal():
    second=e.get()
    e.delete(0,END)
    if calculation=='Addition':
     e.insert(0,fnum+float(second))
    if calculation=='Subtraction':
        e.insert(0,fnum-float(second))
    if calculation=="Multiply":
        e.insert(0,fnum*float(second))
    if calculation=="Divide":
        e.insert(0,fnum/float(second))
    if calculation=="square":
        e.insert(0,math.sqrt(fnum))
    if calculation=="Exponent":
        e.insert(0,fnum**float(second))
    if calculation=="Logarithm":
        e.insert(0,math.log(fnum,10))
    if calculation=="sin":
        e.insert(0,math.sin(math.radians(fnum)))
    if calculation=="cos":
        e.insert(0,math.cos(math.radians(fnum)))
    if calculation=="tan":
        e.insert(0,math.tan(math.radians(fnum)))
        
    
    
    
    
button1=Button(root,text="1",bg="grey",fg="white",padx=49,pady=20,command= lambda: click(1))
button2=Button(root,text="2",bg="grey",fg="white",padx=54,pady=20,command= lambda: click(2))
button3=Button(root,text="3",bg="grey",fg="white",padx=50,pady=20,command= lambda: click(3))
button4=Button(root,text="4",bg="grey",fg="white",padx=49,pady=20,command= lambda: click(4))
button5=Button(root,text="5",bg="grey",fg="white",padx=54,pady=20,command=lambda :click(5))
button6=Button(root,text="6",bg="grey",fg="white",padx=50,pady=20,command=lambda :click(6))
button7=Button(root,text="7",bg="grey",fg="white",padx=49,pady=20,command=lambda :click(7))
button8=Button(root,text="8",bg="grey",fg="white",padx=54,pady=20,command=lambda :click(8))
button9=Button(root,text="9",bg="grey",fg="white",padx=50,pady=20,command=lambda :click(9))
button0=Button(root,text="0",bg="grey",fg="white",padx=49,pady=20,command= lambda: click(0))
buttonclear=Button(root,text="clear",bg="grey",fg="white",padx=101.5,pady=20,command=clear)
buttonadd=Button(root,text="+",bg="grey",fg="white",padx=48,pady=20,command=add)
buttonequal=Button(root,text="=",bg="grey",fg="white",padx=49,pady=20,command=equal)
buttonsub=Button(root,text="-",bg="grey",fg="white",padx=54.4,pady=20,command=subtraction)
buttonmul=Button(root,text="*",bg="grey",fg="white",padx=49.499,pady=20,command=multiply)
buttondiv=Button(root,text="/",bg="grey",fg="white",padx=54.499999,pady=20,command=divide)
buttonsqrt=Button(root,text="sqrt",bg="grey",fg="white",padx=43,pady=20,command=square)
buttonexp=Button(root,text="^",bg="grey",fg="white",padx=48,pady=20,command=exponent)
buttonlog=Button(root,text="log",bg="grey",fg="white",padx=48.41,pady=20,command=logarithm)
buttonsin=Button(root,text="sin",bg="grey",fg="white",padx=45,pady=20,command=sinangle)
buttoncos=Button(root,text="cos",bg="grey",fg="white",padx=43,pady=20,command=cosangle)
buttontan=Button(root,text="tan",bg="grey",fg="white",padx=48,pady=20,command=tanangle)

buttonoff=Button(root,text="OFF",bg="grey",fg="white",padx=42.5,pady=20,command=off)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonclear.grid(row=4,column=1,columnspan=2)
buttonadd.grid(row=5,column=0)
buttonequal.grid(row=5,column=2)
buttonsub.grid(row=5,column=1)
buttonmul.grid(row=6,column=0)
buttondiv.grid(row=6,column=1)
buttonsqrt.grid(row=6,column=2)
buttonexp.grid(row=7,column=0)
buttonlog.grid(row=7,column=1)
buttonsin.grid(row=7,column=2)
buttoncos.grid(row=8,column=0)
buttontan.grid(row=8,column=1)
buttonoff.grid(row=8,column=2)
root.mainloop()

