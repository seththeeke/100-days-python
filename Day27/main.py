"""
Tkinter User Interface

Advanced Arguments
 - Default Values for a function
 - def my_function(a=1, b=2, c=3):
 - *args - many positional arguments
 - **kwargs - many keyword arguments
  - def function(**kwargs):
      - kwargs is consumed as a dictionary object
"""

import tkinter as tk

window = tk.Tk()
window.title("Hello World")

my_label = tk.Label(text="My Label", font=("Helvetica", 20))
# The pack function allows you to configure how the component is shown on screen
my_label.pack()






# Must end the program
window.mainloop()