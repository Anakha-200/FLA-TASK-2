import tkinter as tk
from tkinter import messagebox

def validate():
    username = entry.get()

    trace = ["q0"]
    state = "q0"

    if len(username) == 0:
        result.config(text="REJECTED", fg="red")
        trace_label.config(text="Trace: q0")
        return

    for ch in username:

        if state == "q0":
            if ch.isalpha() or ch == "_":
                state = "q1"
            else:
                state = "Dead"

        elif state == "q1":
            if ch.isalpha() or ch.isdigit() or ch == "_":
                state = "q1"
            else:
                state = "Dead"

        trace.append(state)

        if state == "Dead":
            break

    if state == "q1":
        result.config(text="ACCEPTED", fg="green")
    else:
        result.config(text="REJECTED", fg="red")

    trace_label.config(text="Trace: " + " → ".join(trace))


root = tk.Tk()
root.title("Username DFA Simulator")
root.geometry("900x500")

left = tk.Frame(root)
left.pack(side="left", padx=20, pady=20)

right = tk.Frame(root)
right.pack(side="right", padx=20)

tk.Label(left, text="Username").pack()

entry = tk.Entry(left, width=30, font=("Arial", 14))
entry.pack(pady=10)

tk.Button(left, text="Validate", command=validate).pack()

result = tk.Label(left, text="", font=("Arial",16))
result.pack(pady=15)

trace_label = tk.Label(left, text="Trace:", justify="left")
trace_label.pack()

canvas = tk.Canvas(right, width=500, height=300, bg="white")
canvas.pack()

canvas.create_line(20,100,70,100,arrow=tk.LAST)

canvas.create_oval(70,70,130,130)
canvas.create_text(100,100,text="q0")

canvas.create_oval(220,70,280,130)
canvas.create_text(250,100,text="q1")

canvas.create_oval(370,70,430,130)
canvas.create_oval(365,65,435,135)
canvas.create_text(400,100,text="Accept")

canvas.create_line(130,100,220,100,arrow=tk.LAST)
canvas.create_text(175,80,text="Letter,_")

canvas.create_line(280,100,370,100,arrow=tk.LAST)
canvas.create_text(325,80,text="End")

canvas.create_arc(220,20,280,80,start=0,extent=300,style=tk.ARC)
canvas.create_line(250,20,245,28)
canvas.create_text(250,5,text="Letter,Digit,_")

root.mainloop()