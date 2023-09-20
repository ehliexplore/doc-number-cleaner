import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


def clean_number(number):
    return ''.join(char for char in number if char.isdigit())

def clean_and_copy(event=None):
    raw_number = text_input.get()
    cleaned_number = clean_number(raw_number)
    result_label.config(text=cleaned_number)
    root.clipboard_clear()
    root.clipboard_append(cleaned_number)
    root.update()


def reset():
    text_input.delete(0, tk.END)
    result_label.config(text="")
    clean_copy_button.config(text="LIMPAR E COPIAR", bg="white")


root = ThemedTk(theme="aquativo")
root.title("Limpador de Número")

# Create widgets
frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label1 = ttk.Label(frame, text='Cole o número do documento:', font=("Arial", 16))
label1.grid(column=0, row=0)

text_input = ttk.Entry(frame, font=("Arial", 32))
text_input.grid(column=0, row=1)
text_input.bind('<Return>', clean_and_copy)  # Bind Enter key main button
text_input.bind('<Tab>', clean_and_copy) # Bind Tab key main button


label2 = ttk.Label(frame, text='Número limpo:', font=("Arial", 16))
label2.grid(column=0, row=2)

result_label = ttk.Label(frame, text='', font=("Arial", 34))
result_label.grid(column=0, row=3)

clean_copy_button = ttk.Button(frame, text='LIMPAR E COPIAR', command=clean_and_copy)
clean_copy_button.grid(column=0, row=4)
clean_copy_button.config(style="")

reset_button = ttk.Button(frame, text='RESET', command=reset)
reset_button.grid(column=0, row=5)
reset_button.config(style="")


# Grid column & row configuration
frame.columnconfigure(0, weight=1)
for i in range(6):
    frame.rowconfigure(i, weight=1)

# Main window grid configuration
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
