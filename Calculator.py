import tkinter
import math

window=tkinter.Tk()
window.title("Calculator")
window.configure(background="purple")
input1=tkinter.Entry(window,width=35,borderwidth=5)
input1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
global operator


def button_work(number):
    evvelki_reqem=input1.get()
    input1.delete(0,tkinter.END)
    input1.insert(0,str(evvelki_reqem)+str(number))  
    
 
def button_beraber():
    global operator
    global a1
    global a2
    a2=int(input1.get())
    input1.delete(0,tkinter.END)
    if operator=='ustegel':
        input1.insert(0,a1+a2)
    elif operator=='cixma':
        input1.insert(0,a1-a2)
    elif operator=='vurma':
        input1.insert(0,a1*a2)
    elif operator=='bolme':
        input1.insert(0,a1/a2)
    
    
def button_ustegel():
    global operator
    global a1
    operator="ustegel"
    a1=int(input1.get())
    input1.delete(0,tkinter.END)

def button_cixma():
    global operator
    global a1
    operator="cixma"
    a1=int(input1.get())
    input1.delete(0,tkinter.END)

def button_bolme():
    global operator
    global a1
    operator="bolme"
    a1=int(input1.get())
    input1.delete(0,tkinter.END)

def button_vurma():
    global operator
    global a1
    operator="vurma"
    a1=int(input1.get())
    input1.delete(0,tkinter.END)
    
def button_clear():
    input1.delete(0,tkinter.END)
    
def button_sinus():
    try:
        eded = float(input1.get())
        radian = math.radians(eded)
        input1.delete(0, tkinter.END)
        input1.insert(0, round(math.sin(radian), 2))
    except:
        input1.delete(0, tkinter.END)
        input1.insert(0, "Opps!!")
    
def button_cosinus():
    try:
        eded = float(input1.get())
        radian = math.radians(eded)
        input1.delete(0, tkinter.END)
        input1.insert(0, round(math.cos(radian), 2))
    except:
        input1.delete(0, tkinter.END)
        input1.insert(0, "Opps!!")
        
def button_tang():
        try:
            eded = float(input1.get())
            radian = math.radians(eded)
            input1.delete(0, tkinter.END)
            input1.insert(0, round(math.tan(radian), 2))
        except:
            input1.delete(0, tkinter.END)
            input1.insert(0, "Opps!!")

def button_del():
    text = input1.get()
    if text:
        input1.delete(0, tkinter.END)
        input1.insert(0, text[:-1])
        
def sqrt():
    try:
        eded = float(input1.get())
        input1.delete(0, tkinter.END)
        input1.insert(0, round(math.sqrt(eded), 2))
    except:
        input1.delete(0, tkinter.END)
        input1.insert(0, "Opps!")


button_1=tkinter.Button(window, text='1',padx=40, pady=20,command=lambda:button_work(1))
button_2=tkinter.Button(window, text='2',padx=40, pady=20,command=lambda:button_work(2))
button_3=tkinter.Button(window, text='3',padx=40, pady=20,command=lambda:button_work(3))

button_4=tkinter.Button(window, text='4',padx=40, pady=20,command=lambda:button_work(4))
button_5=tkinter.Button(window, text='5',padx=40, pady=20,command=lambda:button_work(5))
button_6=tkinter.Button(window, text='6',padx=40, pady=20,command=lambda:button_work(6))

button_7=tkinter.Button(window, text='7',padx=40, pady=20,command=lambda:button_work(7))
button_8=tkinter.Button(window, text='8',padx=40, pady=20,command=lambda:button_work(8))
button_9=tkinter.Button(window, text='9',padx=40, pady=20,command=lambda:button_work(9))
button_sin=tkinter.Button(window, text='Sin',padx=40, pady=20,command=lambda:button_sinus())
button_cos=tkinter.Button(window, text='Cos',padx=40, pady=20,command=lambda:button_cosinus())
button_tan=tkinter.Button(window, text='Tang',padx=40, pady=20,command=lambda:button_tang())
button_backspace=tkinter.Button(window, text='Del',padx=40, pady=20,command=lambda:button_del())
but_sqrt=tkinter.Button(window, text='√',padx=40, pady=20,command=lambda:sqrt())

button_1.grid(row=3,column=0,sticky='we')
button_2.grid(row=3,column=1,sticky='we')
button_3.grid(row=3,column=2,sticky='we')
button_4.grid(row=2,column=0,sticky='we')
button_5.grid(row=2,column=1,sticky='we')
button_6.grid(row=2,column=2,sticky='we')
button_7.grid(row=1,column=0,sticky='we')
button_8.grid(row=1,column=1,sticky='we')
button_9.grid(row=1,column=2,sticky='we')
button_sin.grid(row=4,column=3,sticky='we')
button_cos.grid(row=5,column=3,sticky='we')
button_tan.grid(row=3,column=3,sticky='we')
but_sqrt.grid(row=2,column=3,sticky='we')

button_ustegel=tkinter.Button(window, text='+',padx=40, pady=20,command=button_ustegel)
button_0=tkinter.Button(window, text='0',padx=40, pady=20,command=lambda:button_work(0))
button_beraber=tkinter.Button(window, text='=',padx=40, pady=20,command=button_beraber)
button_cixma=tkinter.Button(window, text='-',padx=40, pady=20,command=button_cixma)
button_vurma=tkinter.Button(window, text='*',padx=40, pady=20,command=button_vurma)
button_bolme=tkinter.Button(window, text='/',padx=40, pady=20,command=button_bolme)

button_clear=tkinter.Button(window, text="Clear", padx=130, pady=10, bg="green", command=button_clear)
button_clear.grid(row=6, column=0, columnspan=4,sticky='we')

button_0.grid(row=4,column=1,sticky='we')
button_ustegel.grid(row=4,column=0,sticky='we')
button_beraber.grid(row=4,column=2,sticky='we')
button_cixma.grid(row=5,column=0,sticky='we')
button_vurma.grid(row=5,column=1,sticky='we')
button_bolme.grid(row=5,column=2,sticky='we')
button_backspace.grid(row=1,column=3,sticky='we')






window.mainloop()
