from tkinter import *
import time
from Score import Score

tk = Tk()
tk.title("Catcher Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
score = Score(canvas)

tk.update()
time.sleep(3)
