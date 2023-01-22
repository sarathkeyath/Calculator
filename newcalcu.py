from tkinter import *

calc=Tk()
calc.title("Calculator")
calc.geometry("345x320")
icn=PhotoImage(file="cal.png")
calc.iconphoto(True,icn)

operator=""
inputvalue=StringVar()

def click(number):
    global operator
    
    operator=operator+str(number)
    inputvalue.set(operator)

def res():
   global operator
   result=eval(operator)
   inputvalue.set(result)
   operator=""


def clear():
    global operator
    operator=""
    inputvalue.set("")

def back():
    global operator
    n=len(operator)
    operator=operator[0:n-1]
    print(operator)
    inputvalue.set(operator)




# fr=Frame(calc,height=500,width=400,highlightbackground="grey",highlightthickness=5)
# fr.place(x=250,y=250)
en1=Entry(calc,textvariable=inputvalue,font=("pirulen",20,"bold"),bd=20,fg="#579BB1",bg="#EAF6F6",justify=LEFT,insertwidth=30).grid(row=0,column=0,columnspan=4)
b1=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="1",command=lambda: click(1)).grid(row=1,column=0)
b2=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="2",command=lambda: click(2)).grid(row=1,column=1)
b3=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="3",command=lambda: click(3)).grid(row=1,column=2)
badd=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="+",command=lambda: click("+")).grid(row=1,column=3)


b4=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="4",command=lambda: click(4)).grid(row=2,column=0)
b5=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="5",command=lambda: click(5)).grid(row=2,column=1)
b6=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="6",command=lambda: click(6)).grid(row=2,column=2)
bsub=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="-",command=lambda: click("-")).grid(row=2,column=3)

b7=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="7",command=lambda: click(7)).grid(row=3,column=0)
b8=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="8",command=lambda: click(8)).grid(row=3,column=1)
b9=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="9",command=lambda: click(9)).grid(row=3,column=2)
bmul=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="*",command=lambda: click("*")).grid(row=3,column=3)



bclear=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="C",command=clear).grid(row=4,column=2)
b0=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="0",command=lambda: click(0)).grid(row=4,column=0)
bresult=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="=",command=res).grid(row=4,column=1)
bdiv=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="/",command=lambda: click("/")).grid(row=4,column=3)
b=Button(calc,padx=10,bg="#EAF6F6",fg="black",font=("pirulen",20,"bold"),bd=4,text="B",command=back).grid(row=4,column=4)


calc.mainloop()