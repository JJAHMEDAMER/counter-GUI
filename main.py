import tkinter as tk

x = 0
win = tk.Tk()

number = tk.Label(win, text = x)
number.grid(row= 1, column=1, columnspan=2)

increment = tk.Button(win, text = "INCREMENT", width=20)
increment.grid(row = 2, column = 1)

decrement = tk.Button(win, text = "DECREMENT", width=20)
decrement.grid(row=2, column=2)

win.mainloop()
