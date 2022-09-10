import tkinter as tk
from tkinter.font import Font

BG_COLOR = "#05445E"
BUTTON_COLOR = "#189AB4"
TEXT_COLOR = "#E9ECF5"

BUTTON_WIDTH = 15
BUTTON_HEIGHT = 2

def plus_one():
    global x
    x += 1
    number.config(text = x)
    number.place(relx=0.5, rely=0.5, anchor="center")    
    
def minus_one():
    global x
    x -= 1
    number.config(text = x)
    number.place(relx=0.5, rely=0.5, anchor="center")

x = 0
win = tk.Tk()
win.title("Counter")
win.geometry("400x400")
win.configure(bg=BG_COLOR)
win.grid_propagate(False)

number_font = Font(
    family="Helvetica",
    size = 150,
    weight="bold",
)

button_font = Font(
    family="Helvetica",
    size = 12,
    weight="bold",
)

frame = tk.LabelFrame(win, bg= BG_COLOR, bd = 0, width=350, height=350)
frame.place(relx=0.5, rely=0.5, anchor="center")

number = tk.Label(
    frame, 
    text = x, 
    font=number_font,
    bg = BG_COLOR,
    bd = 0,
    fg = TEXT_COLOR
    )
number.place(relx=0.5, rely=0.4, anchor="center")

increment = tk.Button(
    frame, 
    text = "INCREMENT",
    bg = BUTTON_COLOR, 
    fg = TEXT_COLOR, 
    bd = 0,  
    font=button_font, 
    width=BUTTON_WIDTH, 
    height=BUTTON_HEIGHT, 
    command=plus_one
    )

increment.place(relx=0.2, rely=0.8, anchor="n")

decrement = tk.Button(
    frame, 
    text = "DECREMENT",
    bg = BUTTON_COLOR, 
    fg = TEXT_COLOR, 
    bd = 0, 
    font=button_font, 
    width=BUTTON_WIDTH, 
    height=BUTTON_HEIGHT, 
    command=minus_one
    )

decrement.place(relx=0.8, rely=0.8, anchor="n")

win.mainloop()