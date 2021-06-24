import random
import os
import time


def clear():
    clear = "\n" * 100
    print(clear)


def instruction():
    print()
    print("Правила игры камень-ножницы-бумага : ")
    print()
    print("Камень бьёт ножницы")
    print("Бумага бьёт камень")
    print("Ножницы бьют бумагу")
    print()


def game():
    global table
    global map
    global name

    while True:
        print("--------------------------------------")
        print("\t\tМеню")
        print("--------------------------------------")
        print("Введите \"Правила\" чтобы понять, как в нее играть")
        print("Введите \"Камень\",\"Ножницы\",\"Бумага\" чтобы начать")
        print("Введите \"Выход\" чтобы закончить игру")
        print("--------------------------------------")

        print()

        inp = input("Введите Ваше действия: ")

        if inp.lower() == "правила":
            clear()
            instruction()
            time.sleep(5)
            continue
        elif inp.lower() == "выход":
            clear()
            break
        elif inp.lower() == "камень":
            playermove = 0
        elif inp.lower() == "бумага":
            playermove = 1
        elif inp.lower() == "ножницы":
            playermove = 2
        else:
            clear()
            print("Неверный ввод")
            time.sleep(4)
            continue

        print("Компьютер делает ход....")
        print()
        time.sleep(2)

        computermove = random.randint(0, 2)
        print("Компьютер выбрал ", map[computermove].upper())
        winner = table[playermove][computermove]

        if winner == playermove:
            print(name, "победил!!!")
        elif winner == computermove:
            print("Компьютер выиграл!!!")
        else:
            print("Ничья")

        print()
        time.sleep(5)
        clear()

map = {0: "камень", 1: "бумага", 2: "ножницы"}
table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]
name = input("Введите Ваше имя: ")

while True:
    print()
    print("Начнём игру!!!")
    print("Введите 1, чтобы начать игру")
    print("Введите 2, чтобы выйти")
    print()

    try:
        choice = int(input("Введите Ваш выбор = "))
    except ValueError:
        clear()
        print("Неверный выбор")
        continue
    if choice == 1:
        clear()
        game()
    elif choice == 2:
        print("Пока)")
        break
    else:
        clear()
        print("Неверый выбор, прочитай инструкцию")
