# Палиндромы
word = input('Hello, pls write word: ')
if word == ''.join(reversed(word)):
    print("It's palindrome")
else:
    print("It isn't palindrome")

    # Таблица умножения
number = int(input('Pls write number: '))
for i in range(1, 11):
    print(f'{i} * {number} = {i * number}')

    # Сдаем бутылки
print("Wellcome to bottle drop-off point")
bottle1 = int(input('How many small bottles you want pass: '))
bottle2 = int(input('How many big bottles you want pass: '))

sum = str(bottle1 * 0.10 + bottle2 * 0.25)
if not sum.endswith('0') and not sum.endswith('5'):
    sum += '0'
else:
    pass

print(f'You earned ${sum}')

# Налоги и чаевые
check = float(input('Enter sum of your check: '))


def toFixed(numObj):
    return f"{numObj:.{2}f}"  # Я нашел эту функция в интернете


tips = check * 0.18
tax = check * 0.10  # Налоговая ставка 10%
total = check + tax + tips

print(f'''Check - {toFixed(check)}
Tips - {toFixed(tips)}
Tax - {toFixed(tax)}
Total - {toFixed(total)}
''')

# Сумма первых n подожительных чисел
number = int(input("До какого числа ввести подсет: "))
sum = (number * (number + 1)) / 2

print(f'Сумма чисел от 1 до {number} = {sum}')

# Сувениры и безделушки
print('Wellcome in internet shop')
souvenirs = int(input('How many souvenirs do you need: '))
bauble = int(input('How many baubles do you need: '))

print(f'Total weight of your shopping - {souvenirs * 75 + bauble * 112}g')
