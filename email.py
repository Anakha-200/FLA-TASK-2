import tkinter as tk
import re

# Email validation
def validate():
    email = entry.get()

    pattern = r'^[A-Za-z_][A-Za-z0-9_]*@[A-Za-z0-9-]+\.[A-Za-z]{2,}$'

    if re.match(pattern, email):
        result.config(text="✅ ACCEPTED", fg="green")
    else:
        result.config(text="❌ REJECTED", fg="red")

# Window
root = tk.Tk()
root.title("Email DFA Validator")
root.geometry("700x400")

tk.Label(root, text="Enter Email", font=("Arial",14)).pack()

entry = tk.Entry(root, width=35, font=("Arial",14))
entry.pack(pady=10)

tk.Button(root, text="Validate", command=validate).pack()

result = tk.Label(root, text="", font=("Arial",18))
result.pack(pady=10)

# DFA Diagram
canvas = tk.Canvas(root, width=650, height=180, bg="white")
canvas.pack()

# Start arrow
canvas.create_line(20,90,60,90,arrow=tk.LAST)

# States
canvas.create_oval(60,60,110,110)
canvas.create_text(85,85,text="q0")

canvas.create_oval(180,60,230,110)
canvas.create_text(205,85,text="q1")

canvas.create_oval(300,60,350,110)
canvas.create_text(325,85,text="q2")

canvas.create_oval(420,60,470,110)
canvas.create_text(445,85,text="q3")

canvas.create_oval(540,60,590,110)
canvas.create_oval(545,65,585,105)
canvas.create_text(565,85,text="q4")

# Transitions
canvas.create_line(110,85,180,85,arrow=tk.LAST)
canvas.create_text(145,70,text="Letter/_")

canvas.create_line(230,85,300,85,arrow=tk.LAST)
canvas.create_text(265,70,text="@")

canvas.create_line(350,85,420,85,arrow=tk.LAST)
canvas.create_text(385,70,text="Domain")

canvas.create_line(470,85,540,85,arrow=tk.LAST)
canvas.create_text(505,70,text=".")

# Self-loop on q1
canvas.create_arc(170,20,240,70,start=0,extent=300,style=tk.ARC)
canvas.create_text(205,10,text="Letter/Digit/_")

# Self-loop on q3
canvas.create_arc(410,20,480,70,start=0,extent=300,style=tk.ARC)
canvas.create_text(445,10,text="Letter/Digit")

# Self-loop on q4
canvas.create_arc(530,20,600,70,start=0,extent=300,style=tk.ARC)
canvas.create_text(565,10,text="Letter")

root.mainloop()