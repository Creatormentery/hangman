import random

words = ['кіт', 'собака', 'голуб', 'носоріг', 'папуга', 'змія', 'жирафа', 'жаба', 'щур', 'капібара', 'свиня', 'корова', 'качка', 'кролик', 'страус', 'мавпа']

word = random.choice(words)

def hangman(word):
    wrong = 0
    stages = [
        "__________              ",
        "|                       ",
        "|         |             ",
        "|         |             ",
        "|         O             ",
        "|        /|\            ",
        "|        / \            ",
        "|                       ",
        "|_______________        "
        ]
    rletters = list(word)
    board = [" __ "] * len(word)
    win = False
    print("Ласкаво просимо на страту!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введіть літеру: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if " __ " not in board:
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("Ви програли! Було загадани слово {}.".format(word))
        
hangman(word)
