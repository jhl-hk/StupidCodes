# Import GUI lib tkinter
import tkinter as tk
app = tk.Tk()

# Variables
output_value = 0
output_string = tk.StringVar()
output_string.set("0")

# GUI Settings
app.title("Calculator")

# Functions
def get_current_value():
    current_value = output_string.get()
    return current_value

def number_1_click():
    print("Button 1 clicked")

# GUI Buttons
output = tk.Label(app, textvariable=output_string)
number_key_1 = tk.Button(app, text="1", command=number_1_click)
number_key_2 = tk.Button(app, text="2", command=lambda: print("2"))
number_key_3 = tk.Button(app, text="3", command=lambda: print("3"))
number_key_4 = tk.Button(app, text="4", command=lambda: print("4"))
number_key_5 = tk.Button(app, text="5", command=lambda: print("5"))
number_key_6 = tk.Button(app, text="6", command=lambda: print("6"))
number_key_7 = tk.Button(app, text="7", command=lambda: print("7"))
number_key_8 = tk.Button(app, text="8", command=lambda: print("8"))
number_key_9 = tk.Button(app, text="9", command=lambda: print("9"))

# GUI Layouts
output.grid(row=0, column=2)
number_key_1.grid(row=1, column=0)
number_key_2.grid(row=1, column=1)
number_key_3.grid(row=1, column=2)
number_key_4.grid(row=2, column=0)
number_key_5.grid(row=2, column=1)
number_key_6.grid(row=2, column=2)
number_key_7.grid(row=3, column=0)
number_key_8.grid(row=3, column=1)
number_key_9.grid(row=3, column=2)

app.mainloop()