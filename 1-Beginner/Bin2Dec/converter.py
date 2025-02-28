'''
   Autor: Bruno Franciosi
   Programa: Conversor de binário para decimal
'''
import re
from tkinter import *

def binary_to_decimal(bin):
    bin = list(map(int, bin))
    try:
        decimal = 0
        for i in range(len(bin)):
            decimal += bin[i] * 2**(len(bin)-1-i)
        return decimal
    except ValueError:
        return "Invalid input"

def convert():
    bin = entry.get()
    result = binary_to_decimal(bin)
    result_label.config(text=f"Decimal number: {result}")

def validate_input(new_value):
    return bool(re.fullmatch(r"[01]{0,8}", new_value))



window = Tk()
window.title("Binary to Decimal")
window.geometry('350x100')

text = Label(window, text="Enter a binary number:")
text.grid(column=0, row=0, padx=10, pady=10)

x = window.register(validate_input)  # Registra a função de validação
entry = Entry(window, validate="key", validatecommand=(x, "%P"))
entry.grid(column=1, row=0, padx=10, pady=10)

button = Button(window, text="Convert", command=convert)
button.grid(column=2, row=0, padx=10, pady=10)

result_label = Label(window, text="Decimal number:")
result_label.grid(column=0, row=1, padx=10, pady=10)

window.mainloop()

