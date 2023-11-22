import os

file_path = "fisier.txt"

if os.path.exists(file_path):
    with open("fisier.txt", 'r') as file:
        C = file.read()

    old_word = input("Scrie cuvantul pe care vrei sa il inlocuiesti: ")
    new_word = input("Scrie cuvantul nou pe care il adaugam in propozitie: ")
    cnt = 0

    lista = C.split()

    for i in range(len(lista)):
        if lista[i] == old_word:
            cnt +=1
            lista.pop(i)
            lista.insert(i, new_word)

    with open("fisier.txt", 'w') as file:
        text=','.join(lista)
        file.write(text)


    if cnt == 0:
        print("Nu exista acel cuvant in propozitie")
    else:
        print("Cuvantul a fost inlocuit de", cnt, "ori")
else:
    print(f"Fișierul '{file_path}' nu există.")

