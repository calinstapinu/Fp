from comenzi_taste import *
from alfabetul import *
import turtle

# functie de desenare a caracterului custom daca acesta nu exista deja in dictionarul predefinit sau updatat
def draw_automatically():
    word = input("Scrie cuvantul dorit:")
    for char in word:
        if char in char_dict:
            char_dict[char]()
        else:
            for char in char_dict_new[char]:
                if char == 'w':
                    draw_forward()
                if char == 's':
                    draw_backward()
                if char == 'd':
                    turn_right()
                if char == 'a':
                    turn_left()
                if char == 'f':
                    pick_up()
                if char == 'g':
                    turn_down()

    turtle.done()


def draw_manually():
    print('''
    Utilizați următoarele comenzi:
        W - Stiftul se deplasează înainte cu 10 pixeli
        S - Stiftul se deplasează înapoi cu 10 pixeli
        D - Stiftul se rotește la dreapta cu 45 de grade
        A - Stiftul se rotește la stânga cu 45 de grade
        F - Ridică stiftul (oprește desenul)
        G - Coborâți stiftul (continuați desenul)
    ''')
    newchar = input("Scrieti noul caracter dorit: ")

    with open("taste_apasate.txt", "a") as file:
        file.write(f"{newchar} : ")
    keys()
    turtle.listen()
    turtle.done()


def main():
    with open("taste_apasate.txt", "a") as file:
        file.write("\n")
    print('''
    Alegeti modalitatea de a desena:
    1 - Desen Custom Manual
    2 - Desen Automat
    ''')

    opt = int(input())
    if opt == 2:
        draw_automatically()
    else:
        if opt == 1:
            draw_manually()


main()

