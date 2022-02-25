            #однорукий бандит
from random import randint
# import time
import termcolor
print(termcolor.colored('*' * 32, 'red'))
print(termcolor.colored('Добро пожаловать, в наше казино!', 'red'))
print(termcolor.colored('*' * 32, 'red'))


money = 10000
bank_casino = 1000000
bank = 0
credit = 0
def credit_money():
    valid = True
    global bank_casino

    global money
    global credit
    while valid:
        try:
            credit = int(input(termcolor.colored('Введите ставку: ','green')))
        except:
            print('Неккоректный ввод. Введите цифру')
            continue
        if credit < 500:
            print('Минимальная ставка 500')
            continue
        if (money -credit) < 0:
            print(f'Ваш баланс меньше нуля {money}')
            continue

        money -= credit

        print(termcolor.colored(f'Ваш баланс {money} у.е.','cyan' ))
        print(termcolor.colored(f'Ваша ставка {credit} у.е.', 'cyan'))
        # valid = False

        valid= False



def draw_board():
    input(termcolor.colored('Дерните за рычаг нажав Enter: ','yellow'))
    board = list(range(1, 5))
    board[0] = randint(1,5)
    board[1] = randint(1,5)
    board[2] = randint(1,5)
    board[3] = randint(1,5)

    # time.sleep(2)
    print(termcolor.colored('-' * 17, 'blue'))
    print('|', board[0], '|', board[1],'|', board[2], '|', board[3], '|')
    print(termcolor.colored('-' * 17, 'magenta'))
    return board


def chek_win():
    global bank_casino
    global bank
    global money
    global credit
    credit_money()
    wow = True
    while wow:

        new_board = draw_board()
        if new_board[0] == new_board[1] and new_board[1] == new_board[2] and new_board[2] == new_board[3]:
            if new_board[0] == 1:
                bank_casino = bank_casino - credit * 1
                print(f'Неплохо!{bank}')
            elif new_board[0] == 2:
                bank = bank_casino - credit * 2
                print(f'Вы выиграли! Ставка х2 {bank}')
            elif new_board[0] == 3:
                bank = bank_casino - credit * 3
                print(f'Вы выиграли! Ставка х3 {bank}')
            elif new_board[0] == 4:
                bank = bank_casino - credit * 4
                print(f'Вы выиграли! Ставка х4 {bank}')
            elif new_board[0] == 5:
                bank = bank_casino - credit * 5
                print(f'Джекпот! Ставка х5 {bank}')
        elif new_board[0] == new_board[2] or new_board[1] == new_board[3]:
            print(termcolor.colored('Еще попытка!', 'yellow'))

            continue
        else:
            bank_casino += credit
            print(termcolor.colored('Какая жалость, Вы проиграли!', 'cyan'))
            print(termcolor.colored(f'В банке казино {bank_casino} у.е.', 'cyan'))
            print(termcolor.colored(f'Ваш банк {bank} у.е.', 'cyan'))
            print(termcolor.colored(f'Ваш баланс {money} у.е.', 'cyan'))
        wow = False

chek_win()
c = True
while c:
    x = input(termcolor.colored('Продолжить игру? Нажмите y/n: ', 'magenta'))
    if x == 'y':

        chek_win()
    elif x == 'n':

        print(termcolor.colored(f'Ваш выигрыш {bank} у.е.', 'green'))
        print(termcolor.colored(f'В казино осталось {bank_casino} у.е.', 'green'))
        print(termcolor.colored(f'Ваш баланс составляет: {money} у.е.', 'green'))
        c = False
