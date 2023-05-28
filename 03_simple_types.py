num_1 = 2
num_2 = 0.5
print(num_1 + num_2)

name = 'Дмитрий'
print(f'Привет, {name}!')

num_input = int(input('Введите число от 1 до 10: '))
print(num_input + 10)

user = input('Введите Ваше имя: ')
print(f'Привет, {user}! Как дела?')

print(float('1'))   # 1.0
print(int('2.5'))   # ValueError: invalid literal for int() with base 10: '2.5'
print(bool(1))      # True
print(bool(''))     # False
print(bool(0))      # False