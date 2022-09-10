import tkinter as tk

x = 0
win = tk.Tk()

number = tk.Label(win, text = x)
number.pack()

increment = tk.Button(win, text = "INCREMENT", width=20)
increment.pack()

decrement = tk.Button(win, text = "DECREMENT", width=20)
decrement.pack()
win.mainloop()