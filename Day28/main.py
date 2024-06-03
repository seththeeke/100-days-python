"""
The Pomodoro Technique
"""

import tkinter as tk

FIVE_MINUTES = 5 * 60
TWENTY_FIVE_MINUTES = 25 * 60
TWENTY_MINUTES = 20 * 60



def start():
    count_down()
    pass


def reset():
    pass


def count_down():
    curr_timer -= 1
    print(curr_timer)
    window.after(1000, count_down)

start_timer = TWENTY_FIVE_MINUTES
curr_timer = start_timer

window = tk.Tk()
window.title("Pomodoro Technique")

button = tk.Button(text="Start", command=start)
button.pack()

button = tk.Button(text="Reset", command=reset)
button.pack()

window.mainloop()
