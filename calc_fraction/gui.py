from tkinter import *
from tkinter import ttk


class Gui(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.operations = ['+', '-', '*', '/', 'clear']
        self.master.title("Калькулятор простых дробей")
        self.declareWidget()
        self.placeWidget()


    def declareWidget(self):
        self.integer_1 = ttk.Entry(width=5, font=15, justify=RIGHT)
        self.numerator_1 = ttk.Entry(width=5, font=15, justify=RIGHT)
        self.denominator_1 = ttk.Entry(width=5, font=15, justify=RIGHT)

        self.integer_2 = ttk.Entry(width=5, font=15, justify=RIGHT)
        self.numerator_2 = ttk.Entry(width=5, font=15, justify=RIGHT)
        self.denominator_2 = ttk.Entry(width=5, font=15, justify=RIGHT)


        self.sign_math_oper = ttk.Label(anchor='c', text='...', width=2, font="Arial 19")
        self.label_equal_sign = ttk.Label(anchor='c', text='=', width=2, font="Arial 19")
        self.label_put_minus_sign = ttk.Label(anchor='e', text=' ', width=2, font="Arial 19")

        self.label_integer = ttk.Label(anchor='w', text=0, width=3, font="Arial 14")
        self.label_numerator = ttk.Label(anchor='w', text=0, width=5, font="Arial 14")
        self.label_denominator = ttk.Label(anchor='w', text=0, width=5, font="Arial 14")

        self.fraction_1 = self.integer_1, self.numerator_1, self.denominator_1
        self.fraction_2 = self.integer_2, self.numerator_2, self.denominator_2
        self.fraction = self.fraction_1, self.fraction_2  # создаем многомерный кортеж с дробеми 1 и 2

        self.label_fields = self.label_integer, self.label_numerator, self.label_denominator


    def placeWidget(self):
        self.integer_1.grid(row=1, column=0, rowspan=2, padx=2, pady=4)
        self.numerator_1.grid(row=1, column=1, padx=2, pady=4)
        self.denominator_1.grid(row=2, column=1, padx=2, pady=4)

        self.integer_2.grid(row=1, column=3, rowspan=2, padx=2, pady=4)
        self.numerator_2.grid(row=1, column=4, padx=2, pady=4)
        self.denominator_2.grid(row=2, column=4, padx=2, pady=4)

        self.sign_math_oper.grid(row=1, column=2, rowspan=2, padx=2, pady=4)
        self.label_equal_sign.grid(row=1, column=5, rowspan=2)
        self.label_put_minus_sign.grid(row=1, column=6, rowspan=2)

        self.label_integer.grid(row=1, column=7, rowspan=2)
        self.label_numerator.grid(row=1, column=8)
        self.label_denominator.grid(row=2, column=8)
