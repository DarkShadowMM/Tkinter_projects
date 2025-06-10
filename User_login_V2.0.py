import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title('User_login V2.0')
window.geometry()


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))
    
entry = tk.Entry(window, width=60, borderwidth=2,relief="sunken")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_clear():
    entry.delete(0, tk.END)

def button_login():
    s=entry.get()
    if s=='':
        messagebox.showerror('Error','Something went wrong! Try again!')
        window.destroy()
    else:
        res=messagebox.askyesno("You wrote", s+'?')
        if res:
            messagebox.showinfo('Successful','Successfully loginned in!')
        else:
            messagebox.showwarning('Cancellation','You cancelled the process')

button_a = tk.Button(window, text="a", padx=40, pady=20, command=lambda: button_click('a'))
button_b = tk.Button(window, text="b", padx=40, pady=20, command=lambda: button_click('b'))
button_c = tk.Button(window, text="c", padx=40, pady=20, command=lambda: button_click('c'))
button_d = tk.Button(window, text="d", padx=40, pady=20, command=lambda: button_click('d'))
button_e = tk.Button(window, text="e", padx=40, pady=20, command=lambda: button_click('e'))
button_f = tk.Button(window, text="f", padx=40, pady=20, command=lambda: button_click('f'))
button_g = tk.Button(window, text="g", padx=40, pady=20, command=lambda: button_click('g'))
button_h = tk.Button(window, text="h", padx=40, pady=20, command=lambda: button_click('h'))
button_i = tk.Button(window, text="i", padx=40, pady=20, command=lambda: button_click('i'))
button_j = tk.Button(window, text="j", padx=40, pady=20, command=lambda: button_click('j'))
button_k = tk.Button(window, text="k", padx=40, pady=20, command=lambda: button_click('k'))
button_l = tk.Button(window, text="l", padx=40, pady=20, command=lambda: button_click('l'))
button_m = tk.Button(window, text="m", padx=40, pady=20, command=lambda: button_click('m'))
button_n = tk.Button(window, text="n", padx=40, pady=20, command=lambda: button_click('n'))
button_o = tk.Button(window, text="o", padx=40, pady=20, command=lambda: button_click('o'))
button_p = tk.Button(window, text="p", padx=40, pady=20, command=lambda: button_click('p'))
button_q = tk.Button(window, text="q", padx=40, pady=20, command=lambda: button_click('q'))
button_r = tk.Button(window, text="r", padx=40, pady=20, command=lambda: button_click('r'))
button_s = tk.Button(window, text="s", padx=40, pady=20, command=lambda: button_click('s'))
button_t = tk.Button(window, text="t", padx=40, pady=20, command=lambda: button_click('t'))
button_u = tk.Button(window, text="u", padx=40, pady=20, command=lambda: button_click('u'))
button_v = tk.Button(window, text="v", padx=40, pady=20, command=lambda: button_click('v'))
button_w = tk.Button(window, text="w", padx=40, pady=20, command=lambda: button_click('w'))
button_x = tk.Button(window, text="x", padx=40, pady=20, command=lambda: button_click('x'))
button_y = tk.Button(window, text="y", padx=40, pady=20, command=lambda: button_click('y'))
button_z = tk.Button(window, text="z", padx=40, pady=20, command=lambda: button_click('z'))
button_clear = tk.Button(window, text="Clear", padx=40, pady=20, command=button_clear)
button_login = tk.Button(window, text="Login", padx=40, pady=20, command=button_login)

button_a.grid(row=1, column=0)
button_b.grid(row=1, column=1)
button_c.grid(row=1, column=2)
button_d.grid(row=1, column=3)
button_e.grid(row=1, column=4)
button_f.grid(row=1, column=5)

button_g.grid(row=2, column=0)
button_h.grid(row=2, column=1)
button_i.grid(row=2, column=2)
button_j.grid(row=2, column=3)
button_k.grid(row=2, column=4)
button_l.grid(row=2, column=5)

button_m.grid(row=3, column=0)
button_n.grid(row=3, column=1)
button_o.grid(row=3, column=2)
button_p.grid(row=3, column=3)
button_q.grid(row=3, column=4)
button_r.grid(row=3, column=5)

button_s.grid(row=4, column=0)
button_t.grid(row=4, column=1)
button_u.grid(row=4, column=2)
button_v.grid(row=4, column=3)
button_w.grid(row=4, column=4)
button_x.grid(row=4, column=5)

button_y.grid(row=5, column=0)
button_z.grid(row=5, column=1)
button_clear.grid(row=5,column=2)
button_login.grid(row=5,column=3)

window.mainloop()