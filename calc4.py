import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

screen = tk.StringVar()
screen.set("")

entry = tk.Entry(root, textvar=screen, font=("Arial", 24))
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10)

buttons = [
    ("7",), ("8",), ("9",), ("/",),
    ("4",), ("5",), ("6",), ("*",),
    ("1",), ("2",), ("3",), ("-"),
    ("0",), (".",), ("=",), ("+"),
    ("C",),
]

button_frame = tk.Frame(root)
button_frame.pack()

row_index = 1
col_index = 0

for (text,) in buttons:
    if col_index % 4 == 0 and col_index > 0:
        row_index += 1
        col_index = 0
    
    button = tk.Button(button_frame, text=text, font=("Arial", 18), padx=20, pady=20)
    button.grid(row=row_index, column=col_index, padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)
    
    col_index += 1

root.mainloop()
