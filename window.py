from tkinter import *

window = Tk()
window.title("TkinterExample")

width = 300
height = 500
x = 500
y = 250

window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(False, False)
window.iconbitmap("icon.ico")

window.mainloop()