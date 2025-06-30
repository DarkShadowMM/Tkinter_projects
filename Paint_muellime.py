from tkinter import *
from tkinter import colorchooser

root=Tk()
root.title("Drawing app")

canvas=Canvas(root, width=400, height=400, bg="white")
canvas.pack()

drawing_color= "black"
def set_color_black():
    global drawing_color
    drawing_color="black"
    
def set_color_white(): 
    global drawing_color
    drawing_color="white"
    
def color_picker():
    global drawing_color
    color=colorchooser.askcolor(title="select color")
    if color[1]: 
        drawing_color=color[1]
    
def fill_canvas():
    canvas.create_rectangle(0, 0, 400, 400, fill=drawing_color, outline="")


def clear_canvas(): 
    canvas.delete("all")
    
def paint(event): 
    x1=(event.x-5)
    y1=(event.y-5)
    x2=event.x+5
    y2=(event.y+5)
    
    canvas.create_line(event.x,event.y,event.x+1,event.y+1,width=3,fill=drawing_color)

canvas.bind("<B1-Motion>", paint)

button_frame=Frame(root)
button_frame.pack()

Button(button_frame, text="Draw", command=set_color_black, width=10).pack(side=LEFT)
Button(button_frame, text="Eraser", command=set_color_white, width=10).pack(side=LEFT)
Button(button_frame, text="Color_picker", command=color_picker, width=10).pack(side=LEFT)
Button(button_frame, text="Clear", command=clear_canvas, width=10).pack(side=LEFT)
Button(button_frame, text="Fill", command=fill_canvas, width=10).pack(side=LEFT)

root.mainloop()

