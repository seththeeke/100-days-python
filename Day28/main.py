"""
The Pomodoro Technique
"""

import tkinter as tk

FIVE_MINUTES = 5 * 60
TWENTY_FIVE_MINUTES = 25 * 60
TWENTY_MINUTES = 20 * 60
FIVE_SECONDS = 5

def start():
    count_down(FIVE_SECONDS)


def reset():
    pass


def get_string_time(timer):
    minutes = int(timer / 60)
    seconds = timer % 60
    return f"{minutes}:{seconds}"

def count_down(timer):
    if timer > 0:
        timer -= 1
        label.config(text=f"{get_string_time(timer)}")
        window.after(1000, count_down, timer)


window = tk.Tk()
window.title("Pomodoro Technique")

label = tk.Label(window, text="25:00")
label.pack()

button = tk.Button(text="Start", command=start)
button.pack()

button = tk.Button(text="Reset", command=reset)
button.pack()

window.mainloop()
