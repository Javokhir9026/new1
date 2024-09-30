import tkinter as tk
import colorama
def hisobla():
    try:
        natija = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(natija))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Xato")

def qosh(raqam):
    entry.insert(tk.END, raqam)

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("KALKULYATOR")

entry = tk.Entry(root, width=20, font=('Arial', 24), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

tugmalar = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in tugmalar:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, command=hisobla)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: qosh(t))
    
    button.grid(row=row, column=col)

root.mainloop()
