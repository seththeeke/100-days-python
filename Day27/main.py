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

mile_input = tk.Entry(width=10)
mile_input.pack()

kilo_label = tk.Label(width=10)
kilo_label.pack()


def convert_to_kilos():
    mile_value = float(mile_input.get())
    kilo_value = mile_value * 1.609344
    kilo_label["text"] = str(kilo_value)
    kilo_label.pack()
    pass


button = tk.Button(text="Convert", command=convert_to_kilos)
button["text"] = "Convert"
button.pack()

# Must end the program
window.mainloop()