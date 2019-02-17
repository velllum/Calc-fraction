
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from calc_fraction.gui import Gui


class Frac:
    def __init__(self, gui):
        self.gui = gui # объект файла gui класса Gui
        self.generateButton() # запускаем сгенерированные кнопки
        self.generateNumber() # создаем случайные числа для полей 1 и 2 дроби


    # создание кнопок в придожении
    def generateButton(self):
        for value in self.gui.operations:
            self.b = ttk.Button(width=7, text=value, command=lambda v=value: self.what_operation(v))
            self.b.grid(row=3, column=self.gui.operations.index(value), padx=2, pady=4)


    # распичатать полученый результат на экран
    def output_fraction(self, frac):
        for f, i in zip(self.gui.label_fields, frac):
            f["text"] = int(i)


    # отчистка полей
    def clearFields(self):
        # обнуляем поля ввода
        [i.delete(0, END) for i in (*self.gui.fraction_1, *self.gui.fraction_2)]
        # обнуляем поле вывода
        for i in (self.gui.label_fields):
            i["text"] = 0
        self.gui.sign_math_oper["text"] = '...'
        self.gui.label_put_minus_sign["text"] = ' '


    # подстановка случайных чисел в форму
    def generateNumber(self):
        [i.insert(0, random.randint(1, 10)) for i in (*self.gui.fraction_1, *self.gui.fraction_2)]


    # проверка НОД
    def __gcd(self, a, den, i):
        b = den
        r = i
        while a != 0 and b != 0:
            if a > b or b == a:
                if b == den:
                    r += 1
                a -= b
            else:
                b -= a
        gcd = a + b
        return gcd, r


    # получаем оответ ввиде смешанной дроби
    def reduc_fraction(self, n, d):
        i = 0  # создаем перменную для получения целого числа
        int_gcd = self.__gcd(n, d, i)  # получаем нод и целое число
        gcd = int_gcd[0]  # нод дробей
        integer = int_gcd[1]

        num = n / gcd  # сокращаем числитель
        den = d / gcd  # сокращаем знаменатель

        if num > den:
            num %= den
            if den == 1 and num == 0:
                den = 0
        return integer, num, den


    # получаем наши дроби ([1, 7, 3], [9, 2, 1])
    def both_fractions(self):
        """получаем наши дроби, возвращает ([1, 7, 3], [9, 2, 1])"""
        f = []
        for i in range(len(self.gui.fraction)):
            y = []
            f.append(y)
            for x in range(len(self.gui.fraction[i])):
                y.append(int(self.gui.fraction[i][x].get()))
        return tuple(f)


    # реализация - приводим к неправильной, если есть целая часть
    def improper_fractions(self, i, n, d):
        '''реализация - приводим к неправильной, возвращает [(71, 7), (10, 9)]'''
        num = (i * d) + n
        den = d
        return num, den


    # реализация - приведение занаменателей обеих дробей к общему числу если они не равны
    def common_den(self, d1, d2):
        '''реализация - приведение занаменателей обеих дробей к общему числу если они не равны возращает int'''
        if d1 != d2:
            return d1 * d2
        return d1


    # реализация - умножаем числители обеих дробей используя множители из знаменателя
    def new_num(self, n, d, den):
        '''реализация - умножаем числители обеих дробей используя множители из знаменателя [414, 120] n = числитель, d = знаменатель, den = общий знаменатель (common_den)'''
        num = int(den / d) * n
        return num


    def what_operation(self, value):
        try:
            if value != 'clear':

                # получаем дроби ([1, 7, 3], [9, 2, 1])
                both_frac = self.both_fractions()

                # реализация - приводим к неправильной, возвращает [(71, 7), (10, 9)]
                improper_frac =[self.improper_fractions(*both_frac[i]) for i in range(len(both_frac))]

                # реализация - приведение занаменателей обеих дробей к общему числу возвращает int
                com_den = self.common_den(improper_frac[0][1], improper_frac[1][1])

                # реализация - умножаем числители обеих дробей используя множители из знаменателя [177, 70]
                new_num = [self.new_num(*improper_frac[i], com_den) for i in range(len(improper_frac))]

                # отчистить поле оператора, которое подстовляется перед конечной распечаткой
                self.gui.label_put_minus_sign["text"] = ' '

                # сложение и вычитание
                if value == '-' or value == '+':
                    if value == '-' and new_num[0] < new_num[1]:
                        result_num = eval('new_num[1] {0} new_num[0]'.format(value))
                        # выводим оператор минуса если при вычетании 1-ая дробь меньше 2=ой
                        self.gui.label_put_minus_sign["text"] = '-'
                    else:
                        result_num = eval('new_num[0] {0} new_num[1]'.format(value))
                    result_den = com_den


                # умножение и деление
                if value == '*' or value == '/':
                    if value == '*':
                        result_num = eval('improper_frac[0][0] {0} improper_frac[1][0]'.format(value))
                        result_den = eval('improper_frac[0][1] {0} improper_frac[1][1]'.format(value))
                    else:
                        result_num = eval('improper_frac[0][0] {0} improper_frac[1][1]'.format('*'))
                        result_den = eval('improper_frac[0][1] {0} improper_frac[1][0]'.format('*'))

                # преводим дробь к смешанному виду
                result = self.reduc_fraction(result_num, result_den)


                self.output_fraction(result) # распичатать полученого результата на экран
                self.gui.sign_math_oper["text"] = value # распечать знак математической оперции  на экран

            else:
                # отчистка полей
                self.clearFields()
                self.generateNumber()

        except ValueError:
            messagebox.showerror("Ошибка заполнения", "Ведите в поле коректные данные")


root = Tk()
gui = Gui(root)
Frac(gui)

root.mainloop()
