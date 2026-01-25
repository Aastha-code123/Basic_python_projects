# STEP 1 : IMPORTING
from tkinter import *
from tkinter import ttk

# STEP 2 : GUI INTERACTION
window = Tk()
window.title("Simple Calculator")
window.geometry("315x400")
window.resizable(0,0)
window.configure(bg="#2C3E50")

# ENTRY BOX
entry_box = Entry(window, width=20, borderwidth=5 , font=("Arial", 18),justify="left" ,bg="#ECF0F1", fg="#2C3E50")
entry_box.place(x=5 , y=5)

#BUTTON FUNCTIONALITY

btn_num = {
    "bg": "#34495E",
    "fg": "white",
    "font": ("Arial", 12),
     "activebackground": "#2C3E50",
    "activeforeground": "white"
    
}

btn_op = {
    "bg": "#E67E22",
    "fg": "white",
    "font": ("Arial", 12),
    "activebackground": "#D35400",
    "activeforeground": "white"
    
}

def click(num):
    result = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(result) + str(num))

b = Button(window, text="1",width = 12 , command=lambda: click(1) , **btn_num)
b.place(x=10 , y=60)

b =Button(window, text="2",width = 12, command=lambda: click(2), **btn_num)
b.place(x=100 , y=60)

b= Button(window, text="3",width = 12, command=lambda: click(3), **btn_num)
b.place(x=190 , y=60)

b= Button(window, text="4",width = 12, command=lambda: click(4), **btn_num )
b.place(x= 10 , y=120)

b= Button(window, text="5",width = 12, command=lambda: click(5), **btn_num)
b.place(x=100 , y=120)

b= Button(window, text="6",width = 12, command=lambda: click(6), **btn_num )
b.place(x=190 , y=120)

b=Button(window, text="7",width = 12, command=lambda: click(7), **btn_num)
b.place(x=10 , y=180)

b=Button(window, text="8",width = 12, command=lambda: click(8), **btn_num)
b.place(x=100 , y=180)

b= Button(window, text="9",width = 12, command=lambda: click(9), **btn_num)
b.place(x=190 , y=180)

b= Button(window, text="0",width = 12, command=lambda: click(0), **btn_num)
b.place(x=10 , y=240)


def add():
    n1 = entry_box.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    entry_box.delete(0, END)

b= Button(window, text="+",width = 12, command=add , **btn_op)
b.place(x=100 , y=240)


def subtract():
    n1 = entry_box.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    entry_box.delete(0, END)

b= Button(window, text="-",width = 12, command=subtract, **btn_op)
b.place(x=190 , y=240)


def multiply():
    n1 = entry_box.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    entry_box.delete(0, END)

b= Button(window, text="*",width = 12 , command=multiply, **btn_op)
b.place(x=10 , y=300)


def divide():
    n1 = entry_box.get()
    global math
    math = "division"
    global i
    i = int(n1)
    entry_box.delete(0, END)

b= Button(window, text="/",width = 12 , command=divide  , **btn_op)
b.place(x=100 , y=300)


def equal():
    n2 = entry_box.get()
    entry_box.delete(0, END)
    if math == "addition":
        entry_box.insert(0, i + int(n2))
    elif math == "subtraction":
        entry_box.insert(0, i - int(n2))
    elif math == "multiplication":
        entry_box.insert(0, i * int(n2))
    elif math == "division":
        try :
            entry_box.insert(0, i / int(n2))
        except ZeroDivisionError:
            entry_box.insert(0, "Error")

b= Button(window, text="=",width = 12, command=equal ,  bg="#27AE60", fg="white", font=("Arial", 12),
           activebackground="#1E8449", activeforeground="white")
b.place(x=190 , y=300)


def clear():
    entry_box.delete(0, END)
b= Button(window, text="Clear",width = 12, command=clear ,bg="#E1FB1E",
    fg="black",
    font=("Time New Roman", 12 , "bold"),
    activebackground="#F1EE1A",
    activeforeground="white")

b.place(x=10 , y=350)

# MAINLOOP()
window.mainloop()