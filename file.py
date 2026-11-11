import tkinter as tk
import re

def validate():
    filename = entry.get()

    pattern = r'^[A-Za-z][A-Za-z0-9_-]*\.pdf$'

    if re.fullmatch(pattern, filename):
        result.config(text="✅ ACCEPTED", fg="green")
    else:
        result.config(text="❌ REJECTED", fg="red")

root = tk.Tk()
root.title("PDF File Name Verifier")
root.geometry("700x420")

tk.Label(root, text="Enter File Name", font=("Arial", 14)).pack(pady=10)

entry = tk.Entry(root, width=35, font=("Arial", 14))
entry.pack()

tk.Button(root, text="Verify", command=validate).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 18, "bold"))
result.pack(pady=10)

canvas = tk.Canvas(root, width=650, height=180, bg="white")
canvas.pack()

# Start Arrow
canvas.create_line(20,90,60,90,arrow=tk.LAST)

# States
canvas.create_oval(60,60,110,110)
canvas.create_text(85,85,text="q0")

canvas.create_oval(180,60,230,110)
canvas.create_text(205,85,text="q1")

canvas.create_oval(320,60,370,110)
canvas.create_text(345,85,text="q2")

canvas.create_oval(460,60,510,110)
canvas.create_oval(465,65,505,105)
canvas.create_text(485,85,text="q3")

# Transitions
canvas.create_line(110,85,180,85,arrow=tk.LAST)
canvas.create_text(145,70,text="Letter")

canvas.create_line(230,85,320,85,arrow=tk.LAST)
canvas.create_text(275,70,text=".pdf")

canvas.create_line(370,85,460,85,arrow=tk.LAST)
canvas.create_text(415,70,text="End")

# Self-loop on q1
canvas.create_arc(170,20,240,70,start=0,extent=300,style=tk.ARC)
canvas.create_text(205,10,text="Letter/Digit/_/-")

root.mainloop()