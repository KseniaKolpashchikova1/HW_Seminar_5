# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


# Я знаю, что на лекциях говорили, 
# что нужно к 28 прибавить 1 и выявить остаток от деления 2021 = 20, но это не работает, поэтому только сама игра))

from random import randint

def data_entry(name):
    x = int(input('Введите количество конфет, которое Вы собираетесь взять: '))
    if x < 1 or x > 28:
        x = int(input('Вы ввели некорректное количество конфет. Введите число от 1 до 28:  '))
    return x

def print_result(name, k, count, total_number):
    print(f'Сейчас ходил {name}. Он взял {k} конфет. Всего у него {count} конфет. Остаток {total_number}')

player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')
total_number = int(input('Введите общее количество конфет, находящиеся на столе: '))
priority = randint(0, 2)
if priority:
    print(f'Первым ходит {player_1}')
else:
    print(f'Первым ходит {player_2}')

count_1 = 0
count_2 = 0

while total_number > 0:
    if priority:
        k = data_entry(player_1)
        count_1 += k
        total_number -= k
        priority = False
        print_result(player_1, k, count_1, total_number)
    else:
        k = data_entry(player_2)
        count_2 += k
        total_number -= k
        priority = True
        print_result(player_2, k, count_2, total_number)

if priority:
    print(f'Выигрывает {player_2}')
else:
    print(f'Выигрывает {player_1}')



