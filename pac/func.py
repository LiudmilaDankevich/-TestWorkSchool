# def f(x, y):
#     return x+y
#
# print(f(1, 2))
# from wheel.metadata import yield_lines


# def func():
#     print('Hello world')
#     return 3
#
# a = func
#
# print(a())

# def f(x, y):
#     return x+y
# print(f(1, f(3,4)))

# def power(base, num=None):
#     print(base ** num)
#
# power(10)
# power(5, 3)

# def power(base, num=2):
#     if not isinstance(base, int):
#         return 0
#     return base ** num
#
# print(power(1, 5))
# print(power(2))
# print(power(-1, 1))
# print(power('str'))

# def concat(*args):
#     print(type(args), args)
#     for i in args:
#         print(i)
#     return '-'.join(args)
# print(concat('a', 'b', 'c'))
# print(concat())


# def append_to_dict(dictionary, **kwargs):
#     for key, value in kwargs.items():
#         dictionary[key] = value
#
#     return dictionary
#
#
# a = {"hello": 1, "world": 1}
# print(append_to_dict(a, have=2, nice=1, day=3))


#
# def one_func(x):
#     def two_func(y):
#         return x + y
#     return two_func
#
# x = one_func(5)
# print(x(1))
# Напишите функцию, которая возвращает строку: “Hello world!”
# def hello_fun(a):
#     return a
# print(hello_fun('Hello world!'))

# Напишите функцию, которая вычисляет сумму трех чисел и возвращает результат в основную ветку программы
# def sum_1(a, b, c):
#     return a+b+c
# print(sum_1(4, 5, 1))

# Придумайте программу, в которой из одной функции вызывается
# вторая. При этом ни одна из них ничего не возвращает в
# основную ветку программы, обе должны выводить результаты
# своей работы с помощью функции print().

# def fanc_1(a):
#     def fanc_2(d):
#         return a + d
#     return fanc_2
# x = fanc_1(5)
# print(x(4))

def outer(name):
    def hello(city):
        print('hello ' + name + ' from ' + city)
    return hello
x = outer('Sergey')
print(x('Minsk'))

# Напишите функцию, которая не принимает отрицательные числа.
# и возвращает число наоборот.
# 21445 => 54421
# 123456789 => 987654321

def reverse_num(num:int):
    if isinstance(num, int) and (num > 0):
        num = str(num)
        num = num[::-1]
        return num
print(reverse_num(56789))
print(reverse_num(123))

# У вас интернет магазин, надо написать функцию которая проверяет что введен правильный купон и он еще действителен
#
# def check_coupon(entered_code, correct_code, current_date, expiration_date):
#     #Code here!
#
# check_сoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
# check_сoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False

from datetime import datetime as dt
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    current_date = dt.strptime(current_date, "%B %d, %Y")
    expiration_date = dt.strptime(expiration_date, "%B %d, %Y")
    if (current_date <= expiration_date) and (entered_code == correct_code):
        return True
    else:
        return False
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015"))








