import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        # Initialize variables
        total = 0
        current_number = 0
        operator = '+'
        
        # Iterate over each character in the expression
        for i, char in enumerate(expression):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            if char in "+-*/" or i == len(expression) - 1:
                if operator == '+':
                    total += current_number
                elif operator == '-':
                    total -= current_number
                elif operator == '*':
                    total *= current_number
                elif operator == '/':
                    if current_number == 0:
                        messagebox.showerror("Error", "Cannot divide by zero")
                        return ""
                    total /= current_number
                operator = char
                current_number = 0
        return str(total)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        return ""

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        expression = entry_var.get()
        result = evaluate_expression(expression)
        entry_var.set(result)
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font='Arial 20', bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Keypad buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Arrange buttons in grid
row_val = 1
col_val = 0
for button in buttons:
    button_widget = tk.Button(root, text=button, padx=20, pady=20, font='Arial 18')
    button_widget.grid(row=row_val, column=col_val, sticky='nsew')
    button_widget.bind("<Button-1>", click)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make the buttons expand to fill the available space
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()