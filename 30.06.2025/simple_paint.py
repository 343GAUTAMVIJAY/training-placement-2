import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400, bg='white')
canvas.pack()
last_x, last_y = None, None
def draw(event):
    global last_x, last_y
    if last_x and last_y:
        canvas.create_line(last_x, last_y, event.x, event.y, fill='black')
    last_x, last_y = event.x, event.y
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', lambda e: globals().update(last_x=None, last_y=None))
root.mainloop()