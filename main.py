from ast import Global
import tkinter as tk

def plus_one():
    global x
    x += 1
    number = tk.Label(win, text = x)
    number.grid(row= 1, column=1, columnspan=2)

def minus_one():
    global x
    x -= 1
    number = tk.Label(win, text = x)
    number.grid(row= 1, column=1, columnspan=2)


x = 0
win = tk.Tk()

number = tk.Label(win, text = x)
number.grid(row= 1, column=1, columnspan=2)

increment = tk.Button(win, text = "INCREMENT", width=20, command=plus_one)
increment.grid(row = 2, column = 1)

decrement = tk.Button(win, text = "DECREMENT", width=20, command=minus_one)
decrement.grid(row=2, column=2)
win.mainloop()