__author__ = 'n15001 <n15001@std.it-college.ac.jp>'

from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        pass

ball = Ball(canvas, 'red')

while True:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
