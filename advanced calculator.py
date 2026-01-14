from tkinter import *
import math

# ==== Base Setup ====
window = Tk()
window.title("Advanced Calculator")
window.geometry("400x600")
window.resizable(False, False)

# Theme variables
current_theme = "light"
bg_light = "#ffffff"
bg_dark = "#222222"
fg_light = "#000000"
fg_dark = "#ffffff"
button_color = "#f0f0f0"
button_active = "#dcdcdc"

# ==== Functions ====
equation_text = ""
equation_label = StringVar()

def press(n):
    global equation_text
    equation_text += str(n)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        expression = equation_text.replace("√", "math.sqrt").replace("^", "**")
        total = str(eval(expression))
        equation_label.set(total)
        equation_text = total
    except:
        equation_label.set("error")
        equation_text = ""

def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

def toggle_theme():
    global current_theme
    if current_theme == "light":
        current_theme = "dark"
        window.configure(bg=bg_dark)
        label.config(bg=bg_dark, fg=fg_dark)
        for btn in buttons:
            btn.config(bg="#444", fg="white", activebackground="#555")
    else:
        current_theme = "light"
        window.configure(bg=bg_light)
        label.config(bg=bg_light, fg=fg_light)
        for btn in buttons:
            btn.config(bg=button_color, fg="black", activebackground=button_active)

def keypress(event):
    key = event.char
    if key in "0123456789+-*/.^":
        press(key)
    elif key == "\r":  # Enter
        equals()
    elif key == "\x08":  # Backspace
        backspace()
    elif key == "c":
        clear()
    elif key == "s":  # sqrt shortcut
        press("√")

# ==== UI ====
label = Label(window, font=("Arial", 30), textvariable=equation_label,
              bg=bg_light, fg=fg_light, anchor="e", height=2)
label.pack(fill="both")

frame = Frame(window)
frame.pack()

buttons = []

btn_data = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("^", 4, 2), ("+", 4, 3),
    ("(", 5, 0), (")", 5, 1), ("√", 5, 2), ("=", 5, 3),
]

for (text, row, col) in btn_data:
    cmd = equals if text == "=" else lambda val=text: press(val)
    b = Button(frame, text=text, width=5, height=2, font=("Arial", 18),
               bg=button_color, fg="black", command=cmd)
    b.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    buttons.append(b)

# Make grid responsive
for i in range(6):
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# Extra controls
extra_frame = Frame(window, bg=bg_light)
extra_frame.pack(fill="x", pady=10)

btn_clear = Button(extra_frame, text="Clear", font=("Arial", 16),
                   command=clear, bg=button_color)
btn_clear.pack(side="left", expand=True, fill="x", padx=5)

btn_back = Button(extra_frame, text="⌫", font=("Arial", 16),
                  command=backspace, bg=button_color)
btn_back.pack(side="left", expand=True, fill="x", padx=5)

btn_theme = Button(extra_frame, text="🌓 Theme", font=("Arial", 16),
                   command=toggle_theme, bg=button_color)
btn_theme.pack(side="left", expand=True, fill="x", padx=5)

# Keyboard binding
window.bind("<Key>", keypress)

# Start app
window.mainloop()
