import tkinter as tk

def start_drawing(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    canvas.create_line(last_x, last_y, event.x, event.y, width=2)
    last_x, last_y = event.x, event.y

def stop_drawing(event):
    pass

root = tk.Tk()
root.title("Simple Paint")

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

canvas.bind("<Button-1>", start_drawing)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", stop_drawing)

last_x, last_y = None, None

root.mainloop()
