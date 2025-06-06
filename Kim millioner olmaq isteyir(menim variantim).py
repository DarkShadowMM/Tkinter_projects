import tkinter as tk
from tkinter import messagebox 

sual=[
    ("Azerbaycanin paytaxti haradi?", "Paris", "Bucharest", "Baku", "Berlin", "C"),
    ("2+2 necedir", "3", "4", "5", "6", "B"),
    (" Hamletin yazari kimdir?", "Goethe", "Shakespeare", "Dickens", "Lev Tolstoy", "B")
]
current_sual=0
score=0
def cavab_yoxlanmasi(herf): 
    global current_sual, score

    if herf==sual[current_sual][5]: 
        score+=1
        messagebox.showinfo("Dogru cavab", "Siz duzgun cavab verdiniz!")

    else:
        messagebox.showinfo("title", "information")
        app.destroy()

    current_sual+=1
    if current_sual<len(sual): 
        display_question(current_sual)
    else: 
        messagebox.showinfo("SON!", f"Oyun bitdi. Siz {score}/{len(sual)} bal qazandiniz")
        app.destroy()





def display_question(index):
    question, a,b,c,d,_= sual[index]
    sual_label.config(text=question)
    button_a.config(text="A: "+a)
    button_b.config(text="B: "+b)
    button_c.config(text="C: "+c)
    button_d.config(text="D: "+d)
    
app=tk.Tk()
app.title("Kim Milyoner olmaq Isteyir?")

sual_label=tk.Label(app, text="", width=50, height=3)
sual_label.pack(pady=(20,10))

button_a=tk.Button(app, text="", command= lambda: cavab_yoxlanmasi("A"), width=50)
button_a.pack()

button_b=tk.Button(app, text="", command= lambda: cavab_yoxlanmasi("B"), width=50)
button_b.pack()

button_c=tk.Button(app, text="", command= lambda: cavab_yoxlanmasi("C"), width=50)
button_c.pack()

button_d=tk.Button(app, text="", command= lambda: cavab_yoxlanmasi("D"), width=50)
button_d.pack()

display_question(current_sual)
app.mainloop()
