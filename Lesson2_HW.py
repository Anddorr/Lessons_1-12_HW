from random import randint

print('Приветствую в игре - Камень, ножницы, бумага', end='\n\n')

print('Режимы игры: Против игрока(1), Против бота(2)')
mode = input('Выберите режим игры: ')  # Выбор режима игры
quantity_of_wins = int(input('Выберите до скольки побед будете играть: '))  # Выбор до скольки побед будет идти игра
print('')


def pvp(rounds):  # Функция для игры против игрока
    player1_wins = 0
    player2_wins = 0
    while player1_wins < rounds and player2_wins < rounds:  # Игра с помощью цикла будет идти до момента достижения
        print(
            'Ходы: Камень(1), Ножницы(2), Бумага(3) (Выберайте цифрами)')  # одним из игроков необходимого количества очков

        player1 = int(input('Первый игрок сделайте свой ход: '))
        if player1 != 1 and player1 != 2 and player1 != 3:  # Проверка хода 1го игрока
            print('Вы ввели невозможный ход, введите ход из списка')
            player1 = int(input('Первый игрок сделайте свой ход: '))
        else:
            pass

        player2 = int(input('Второй игрок сделайте свой ход: '))
        if player2 != 1 and player2 != 2 and player2 != 3:  # Проверка хода 2го игрока
            print('Вы ввели невозможный ход, введите ход из списка')
            player2 = int(input('Второй игрок сделайте свой ход: '))
        else:
            pass

        if player1 == player2:  # Опредедение ничьи
            print(f'Ничья. Счет - {player1_wins} : {player2_wins}\n\n')
        elif player1 == 1:  # Определения победителя в разных условиях
            if player1 + player2 == 3:
                player1_wins += 1
                print(f'Раунд победил первый игрок. Счет - {player1_wins} : {player2_wins}\n\n')
            else:
                player2_wins += 1
                print(f'Раунд победил второй игрок. Счет - {player1_wins} : {player2_wins}\n\n')
        elif player1 == 2:
            if player1 + player2 == 5:
                player1_wins += 1
                print(f'Раунд победил первый игрок. Счет - {player1_wins} : {player2_wins}\n\n')
            else:
                player2_wins += 1
                print(f'Раунд победил второй игрок. Счет - {player1_wins} : {player2_wins}\n\n')
        else:
            if player1 + player2 == 4:
                player1_wins += 1
                print(f'Раунд победил первый игрок. Счет - {player1_wins} : {player2_wins}\n\n')
            else:
                player2_wins += 1
                print(f'Раунд победил второй игрок. Счет - {player1_wins} : {player2_wins}\n\n')
    if player1_wins > player2_wins:
        print(f'В игре победил Первый игрок со счетом - {player1_wins} : {player2_wins}')  # Объявление победителя
    else:
        print(f'В игре победил Второй игрок со счетом - {player1_wins} : {player2_wins}')


def pvb(rounds):  # Фунция для игры против бота
    player_wins = 0
    bot_wins = 0
    while player_wins < rounds and bot_wins < rounds:
        print('Ходы: Камень(1), Ножницы(2), Бумага(3) (Выберайте цифрами)')

        player = int(input('Игрок сделайте свой ход: '))
        if player != 1 and player != 2 and player != 3:  #
            print('Вы ввели невозможный ход, введите ход из списка')
            player = int(input('Игрок сделайте свой ход: '))
        else:
            pass

        bot = randint(1, 3)  # Рандомизация хода бота
        print(f'Бот ходил {bot}')

        if player == bot:
            print(f'Ничья. Счет - {player_wins} : {bot_wins}\n\n')
        elif player == 1:
            if player + bot == 3:
                player_wins += 1
                print(f'Раунд победил игрок. Счет - {player_wins} : {bot_wins}\n\n')
            else:
                bot_wins += 1
                print(f'Раунд победил бот. Счет - {player_wins} : {bot_wins}\n\n')
        elif player == 2:
            if player + bot == 5:
                player_wins += 1
                print(f'Раунд победил игрок. Счет - {player_wins} : {bot_wins}\n\n')
            else:
                bot_wins += 1
                print(f'Раунд победил бот. Счет - {player_wins} : {bot_wins}\n\n')
        else:
            if player + bot == 4:
                player_wins += 1
                print(f'Раунд победил игрок. Счет - {player_wins} : {bot_wins}\n\n')
            else:
                bot_wins += 1
                print(f'Раунд победил бот. Счет - {player_wins} : {bot_wins}\n\n')

    if player_wins > bot_wins:
        print(f'В игре победил игрок со счетом - {player1_wins} : {player2_wins}')  # Объявление победителя
    else:
        print(f'В игре победил бот со счетом - {player1_wins} : {player2_wins}')


if mode == '1':  # Выбор режима
    pvp(quantity_of_wins)
elif mode == '2':
    pvb(quantity_of_wins)
else:
    print('Такого режима не существует')

print('Игра закончилась!!! ')
