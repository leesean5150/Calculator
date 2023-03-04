import tkinter as tk
from tkinter import messagebox
from math import *

calculation = ''

# functions
# recording and displaying users input
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

# evaluation of users input with error catcher
def evaluate_calculation():
    global calculation
    try:
        # result = str(eval(calculation))
        # calculation = ''
        calculation = str(eval(calculation))
        text_result.delete(1.0, 'end')
        # text_result.insert(1.0, result)
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, 'Error')

# function for clearing calculator screen
def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')

# function to confirm exiting application
def on_closing():
    if messagebox.askyesno(title = 'Quit', message = 'Do you want to exit this application?'):
        root.destroy()


# user interface
# initialization of GUI
root = tk.Tk()
root.geometry('300x275')
root.title('Calculator')

# initialization of calculator screen
text_result = tk.Text(root, height = 2, width = 16, font = ('Arial', 24), state = 'disabled')
text_result.grid(columnspan = 5)


# initialization of buttons
# number buttons
btn_1 = tk.Button(root, text = '1', command = lambda: add_to_calculation(1), width = 5, font = ('Arial', 14))
btn_1.grid(row = 1, column = 0)
btn_2 = tk.Button(root, text = '2', command = lambda: add_to_calculation(2), width = 5, font = ('Arial', 14))
btn_2.grid(row = 1, column = 1)
btn_3 = tk.Button(root, text = '3', command = lambda: add_to_calculation(3), width = 5, font = ('Arial', 14))
btn_3.grid(row = 1, column = 2)
btn_4 = tk.Button(root, text = '4', command = lambda: add_to_calculation(4), width = 5, font = ('Arial', 14))
btn_4.grid(row = 2, column = 0)
btn_5 = tk.Button(root, text = '5', command = lambda: add_to_calculation(5), width = 5, font = ('Arial', 14))
btn_5.grid(row = 2, column = 1)
btn_6 = tk.Button(root, text = '6', command = lambda: add_to_calculation(6), width = 5, font = ('Arial', 14))
btn_6.grid(row = 2, column = 2)
btn_7 = tk.Button(root, text = '7', command = lambda: add_to_calculation(7), width = 5, font = ('Arial', 14))
btn_7.grid(row = 3, column = 0)
btn_8 = tk.Button(root, text = '8', command = lambda: add_to_calculation(8), width = 5, font = ('Arial', 14))
btn_8.grid(row = 3, column = 1)
btn_9 = tk.Button(root, text = '9', command = lambda: add_to_calculation(9), width = 5, font = ('Arial', 14))
btn_9.grid(row = 3, column = 2)
btn_0 = tk.Button(root, text = '0', command = lambda: add_to_calculation(0), width = 5, font = ('Arial', 14))
btn_0.grid(row = 4, column = 1)

# operator buttons
btn_plus = tk.Button(root, text = '+', command = lambda: add_to_calculation('+'), width = 5, font = ('Arial', 14))
btn_plus.grid(row = 1, column = 3)
btn_minus = tk.Button(root, text = '-', command = lambda: add_to_calculation('-'), width = 5, font = ('Arial', 14))
btn_minus.grid(row = 2, column = 3)
btn_multiply = tk.Button(root, text = '*', command = lambda: add_to_calculation('*'), width = 5, font = ('Arial', 14))
btn_multiply.grid(row = 3, column = 3)
btn_divide = tk.Button(root, text = '/', command = lambda: add_to_calculation('/'), width = 5, font = ('Arial', 14))
btn_divide.grid(row = 4, column = 3)
btn_open_bracket = tk.Button(root, text = '(', command = lambda: add_to_calculation('('), width = 5, font = ('Arial', 14))
btn_open_bracket.grid(row = 4, column = 0)
btn_close_bracket = tk.Button(root, text = ')', command = lambda: add_to_calculation(')'), width = 5, font = ('Arial', 14))
btn_close_bracket.grid(row = 4, column = 2)
btn_decimal = tk.Button(root, text = '.', command = lambda: add_to_calculation('.'), width = 5, font = ('Arial', 14))
btn_decimal.grid(row = 5, column = 2)
btn_equal = tk.Button(root, text = '=', command = lambda: evaluate_calculation(), width = 5, font = ('Arial', 14))
btn_equal.grid(row = 5, column = 3)

# QOL buttons
btn_clear = tk.Button(root, text = 'clr', command = lambda: clear_field(), width = 5, font = ('Arial', 14))
btn_clear.grid(row = 5, column = 0)
# btn_clear.grid(row, column, columnspan = 2)
btn_backspace = tk.Button(root, text = '<--', command = lambda: text_result.delete('end-2c'), width = 5, font = ('Arial', 14))
btn_backspace.grid(row = 5, column = 1)


# drop-down menu
# initialize parent menubar
menubar = tk.Menu(root)

# initialize trigonometric function menu
trigo_menu = tk.Menu(menubar, tearoff = 0)
# initialize trigonometric functions
trigo_menu.add_command(label = 'sin()', command = lambda: add_to_calculation('sin('))
trigo_menu.add_command(label = 'cos()', command = lambda: add_to_calculation('cos('))
trigo_menu.add_command(label = 'tan()', command = lambda: add_to_calculation('tan('))
trigo_menu.add_separator
menubar.add_cascade(menu = trigo_menu, label = 'Trigo')

# initialize inverse trigonometric function menu
atrigo_menu = tk.Menu(menubar, tearoff = 0)
# initialize inverse trigonometric functions
atrigo_menu.add_command(label = 'asin()', command = lambda: add_to_calculation('asin('))
atrigo_menu.add_command(label = 'acos()', command = lambda: add_to_calculation('acos('))
atrigo_menu.add_command(label = 'atan()', command = lambda: add_to_calculation('atan('))
atrigo_menu.add_separator
menubar.add_cascade(menu = atrigo_menu, label = 'Inverse')

# initialize transcedental number menu
transcedental_menu = tk.Menu(menubar, tearoff = 0)
# initialize transcedental numbers
transcedental_menu.add_command(label = 'pi', command = lambda: add_to_calculation('pi'))
transcedental_menu.add_command(label = 'e', command = lambda: add_to_calculation('pi'))
transcedental_menu.add_separator
menubar.add_cascade(menu = transcedental_menu, label = 'Transcedental')

# initialize logarithmic function menu
logarithmic_menu = tk.Menu(menubar, tearoff = 0)
# initialize logarithmic functions
logarithmic_menu.add_command(label = 'log', command = lambda: add_to_calculation('log(10,'))
logarithmic_menu.add_command(label = 'ln', command = lambda: add_to_calculation('log(e'))
logarithmic_menu.add_separator
menubar.add_cascade(menu = logarithmic_menu, label = 'Logarithm')


root.config(menu = menubar)


# prompt on_closing function when user tries to close window
root.protocol('WM_DELETE_WINDOW', on_closing)


# execute main code
root.mainloop()