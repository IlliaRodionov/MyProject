# Задание 1
# Напишите функцию, которая отображает на экран форматированный текст, указанный ниже:
# “Don't compare yourself with anyone in this world... if you do so, you are insulting yourself.”

def formatting():
    text1 = "Don't {0} yourself with {1} in this world{2} if you do so, you are insulting yourself."\
        .format("compare", "anyone", "...")
    print(text1)


formatting()

#=====================================================================================================

# Задание 2
# Напишите функцию, которая принимает два числа в качестве параметра и отображает все четные числа между ними.

def counts(a, b):
    values = []
    for count in range(a + 1, b):
        if count % 2 == 0:
            print(count)
            values.append(count)


counts(a=3, b=10)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Задание 3
# Напишите функцию, которая отображает пустой или заполненный квадрат из некоторого символа.
# Функция принимает в качестве параметров:длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный; ■ если False, квадрат пустой.

def square_of_symbols(square_length, symbol, condition_var):
    for z in range(square_length):
        if condition_var:
            # i = 1
            # while i <= square_length:
            print(symbol * square_length)
            # i += 1
        elif z == 0 or z == square_length - 1:
            print(symbol * square_length)
        else:
            print(symbol, ' ' * (square_length - 2), symbol, sep='')


user_length = int(input('Введите длину стороны квадрата: '))
user_symbol = input('Введите символ для заполнения квадрата: ')
user_condition = int(input('Введите 1 для заполнения квадрата и 0 для создания пустого квадрата: '))
square_of_symbols(user_length, user_symbol, user_condition)
