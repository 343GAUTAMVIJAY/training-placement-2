import tkinter as tk

root = tk.Tk()
tasks = []
entry = tk.Entry(root)
entry.pack()
listbox = tk.Listbox(root)
listbox.pack()
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
def remove_task():
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection[0])
        tasks.pop(selection[0])
tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Remove Task", command=remove_task).pack()
root.mainloop()