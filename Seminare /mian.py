import turtle
import json

# Dicționarul cu caractere inițiale
characters = {
    'A': ['forward 100', 'right 45', 'forward 50', 'right 90', 'forward 50', 'right 135', 'forward 100', 'penup',
          'left 90', 'forward 50', 'right 90', 'pendown', 'forward 100', 'penup', 'backward 100', 'left 90',
          'backward 50', 'right 90', 'backward 50', 'left 135', 'backward 100'],
    'B': ['penup', 'forward 100', 'pendown', 'left 90', 'forward 100', 'right 90', 'circle -50 180', 'right 180',
          'circle -50 180', 'right 180', 'forward 100', 'penup', 'left 90', 'forward 50', 'left 90', 'pendown'],
    # Adăugați instrucțiuni pentru alte caractere aici
}

# Funcție pentru a desena un caracter specific
def draw_character(char):
    for action in characters[char]:
        if action.startswith('forward'):
            distance = int(action.split()[-1])
            turtle.forward(distance)
        elif action.startswith('backward'):
            distance = int(action.split()[-1])
            turtle.backward(distance)
        elif action.startswith('right'):
            angle = int(action.split()[-1])
            turtle.right(angle)
        elif action.startswith('left'):
            angle = int(action.split()[-1])
            turtle.left(angle)
        elif action == 'penup':
            turtle.penup()
        elif action == 'pendown':
            turtle.pendown()

# Funcție pentru a adăuga un caracter personalizat în dicționar
def add_custom_character():
    custom_char = input("Introduceți un caracter personalizat (o literă sau un simbol): ")
    if custom_char.isalnum() and custom_char not in characters:
        custom_instructions = input("Introduceți instrucțiunile de desenare pentru caracterul personalizat: ")
        characters[custom_char] = custom_instructions.split()

# Salvăm dicționarul de caractere într-un fișier JSON
def save_characters():
    with open("characters.json", "w") as file:
        json.dump(characters, file)

# Încărcăm dicționarul de caractere din fișierul JSON la pornirea programului (dacă există)
try:
    with open("characters.json", "r") as file:
        characters = json.load(file)
except FileNotFoundError:
    pass

# Configurare Turtle
turtle.speed(1)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

# Afisare instructiuni pentru utilizator
print("Utilizați următoarele comenzi:")
print("W - Stiftul se deplasează înainte cu 10 pixeli")
print("S - Stiftul se deplasează înapoi cu 10 pixeli")
print("D - Stiftul se rotește la dreapta cu 45 de grade")
print("A - Stiftul se rotește la stânga cu 45 de grade")
print("F - Ridică stiftul (oprește desenul)")
print("G - Coborâți stiftul (continuați desenul)")
print("Pentru a adăuga un caracter personalizat, introduceți \"add\"")

while True:
    user_input = input("Introduceți un mesaj sau o comandă: ").upper()

    if user_input == "":
        break
    elif user_input == "ADD":
        add_custom_character()
    else:
        for char in user_input:
            if char in characters:
                draw_character(char)

# Salvăm dicționarul de caractere personalizate
save_characters()

# Terminăm desenul
turtle.hideturtle()
turtle.done()
