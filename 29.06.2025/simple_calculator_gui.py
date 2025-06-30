import tkinter as tk

def button_click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
for i in range(10):
    tk.Button(root, text=str(i), command=lambda x=i: button_click(x)).pack(side=tk.LEFT)
tk.Button(root, text="=", command=calculate).pack(side=tk.LEFT)
root.mainloop()