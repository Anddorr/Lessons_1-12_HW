from random import randint

print('Wellcome in game "guess the number"\n')

start = int(input('Enter the number from which the generation will start: '))  # Определяем диапозон рандома
end = int(input('Enter the number from which the generation will end: '))

number = randint(start, end)

player_number = int(input(f'Enter a number between {start} and {end}: '))  # Проверка
if number == player_number:
    print('You guessed!!!')
elif number > player_number:
    print('You guessed wrong! Your number is less than the needed one')
    print(f'Guessed number was {number}')
elif number < player_number:
    print('You guessed wrong! Your number is more than the needed one')
    print(f'Guessed number was {number}')
else:
    print(ERROR)
