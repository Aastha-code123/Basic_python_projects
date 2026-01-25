
from tkinter import *

window = Tk()
window.title("To-Do List")
window.geometry("600x550")
window.resizable(0, 0)
window.configure(bg="#183A5C")

# ---------------- TITLE ----------------
label = Label(
    window,
    text="To-Do List",
    bg="#183A5C",
    fg="white",
    font=("Helvetica", 22, "bold")
)
label.pack(pady=(20, 20))

# ---------------- INPUT ----------------
input_frame = Frame(window, bg="#183A5C")
input_frame.pack(pady=5)

entry_box = Entry(
    input_frame,
    width=25,
    borderwidth=5,
    font=("Gotham", 18),
    bg="#ECF0F1",
    fg="#2C3E50"
)
entry_box.pack(side=LEFT, padx=(0, 20))

# ---------------- FILTER BUTTONS ----------------
filter_frame = Frame(window, bg="#183A5C")
filter_frame.pack(pady=10)

# list to store all tasks
tasks = []

#row = task ka UI box ( checkboc , text label , delete button)
#var = task ka status (0 ya 1)

def show_all():
    for task in tasks:
        task["row"].pack(fill="x", pady=5)

def show_completed():
    for task in tasks:
        if task["var"].get() == 1:
            task["row"].pack(fill="x", pady=5)
        else:
            task["row"].pack_forget()

def show_uncompleted():
    for task in tasks:
        if task["var"].get() == 0:
            task["row"].pack(fill="x", pady=5)
        else:
            task["row"].pack_forget()

b=Button(filter_frame, text="All", width=12, command=show_all)
b.pack(side=LEFT, padx=5)

b=Button(filter_frame, text="Completed", width=12, command=show_completed)
b.pack(side=LEFT, padx=5)

b=Button(filter_frame, text="Uncompleted", width=12, command=show_uncompleted)
b.pack(side=LEFT, padx=5)

# ---------------- TASK AREA ----------------
task_frame = Frame(window, bg="#183A5C")
task_frame.pack(pady=10, anchor="w", padx=60)

# ---------------- ADD TASK ----------------
def add_task():
    task_text = entry_box.get()
    if task_text == "":
        return

    row = Frame(task_frame, bg="#183A5C")
    row.pack(fill="x", pady=5)

    var = IntVar()

    task_label = Label(
        row,
        text=task_text,
        bg="#183A5C",
        fg="white",
        font=("Arial", 14)
    )
    task_label.pack(side=LEFT)

    def mark_done():
        if var.get() == 1:
            task_label.config(
                fg="#95A5A6",
                font=("Arial", 14, "overstrike")
            )
        else:
            task_label.config(
                fg="white",
                font=("Arial", 14)
            )

    cb = Checkbutton(
        row,
        variable=var,
        bg="#183A5C",
        fg="white",
        font=("Arial", 16, "bold"),
        activebackground="#183A5C",
        selectcolor="#ECF0F1",
        command=mark_done
    )
    cb.pack(side=LEFT , padx=(0,10))

    
    del_btn = Button(
        row,
        text="❌",
        bg="#E74C3C",
        fg="white",
        bd=0,
        command=lambda: remove_task(row)
    )
    del_btn.pack(side=RIGHT , padx=5)

    tasks.append({"row": row, "var": var})
    entry_box.delete(0, END)


def remove_task(row):
    for task in tasks:
        if task["row"] == row:
            tasks.remove(task)
            break
    row.destroy()



# ---------------- ADD BUTTON ----------------
Button(
    input_frame,
    text="+ Add Task",
    width=10,
    bg="#3ABBEF",
    fg="white",
    font=("Times New Roman", 14, "bold"),
    command=add_task
).pack(side=LEFT)

window.mainloop()
