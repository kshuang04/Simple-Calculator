import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

def buttonClick(number):
    curr = entryMain.get()
    entryMain.delete(0,tk.END)
    entryMain.insert(0, str(curr) + str(number))

def buttonEqual():
    try:
        result = eval(entryMain.get())
        entryMain.delete(0, tk.END)
        entryHistory.delete(0, tk.END)
        entryHistory.insert(0, result)
    except:
        entryMain.delete(0, tk.END)
        entryHistory.delete(0, tk.END)
        entryHistory.insert(0, "Error")

def buttonClear():
    entryMain.delete(0, tk.END)

entryMain = tk.Entry(root, width=16, font=("Ariel", 24), justify="right")
entryMain.grid(row=1, column=0, columnspan=4)
entryHistory = tk.Entry(root, width=16, font=("Ariel", 24), justify="right")
entryHistory.grid(row=0, column=0, columnspan=4)


buttons = [
    ("7", 2, 0),("8", 2, 1),("9", 2, 2),("/", 2, 3),
    ("4", 3, 0),("5", 3, 1),("6", 3, 2),("*", 3, 3),
    ("1", 4, 0),("2", 4, 1),("3", 4, 2),("-", 4, 3),
    ("0", 5, 0),(".", 5, 1),("=", 5, 2),("+", 5, 3),
]

for (text, row, col) in buttons:
    cmd = lambda t=text: buttonClick(t)
    if text == "=": cmd = buttonEqual
    tk.Button(root, text=text, command=cmd).grid(row=row, column=col, sticky="nsew")

tk.Button(root, text="Clear", command=buttonClear).grid(row=6, column=0, columnspan=4, sticky="nsew")

root.mainloop()