import random


# functie care determina alegerea calculatorului
def alegere_calculator():
    alegeri = ["Schere", "Stein", "Papier"]
    return random.choice(alegeri)

# functie care determina alegerea userului
def alegere_user():
    print("Alege o optiune:")
    print("1. Schere")
    print("2. Stein")
    print("3. Papier")
    choice = input("Scrie numarul optiunii alese: ")
    choices = ["Schere", "Stein", "Papier"]
    return choices[int(choice) - 1] # -1 deoarece indexarea este de la 0 si sa aleaga pozitile corecte

# functie care compara alegerile facute si determina un castigator pe baza regulilor jocului <3
def gaseste_castigator(user, computer):
    if user == computer:
        return "Egalitate"
    elif (user == "Schere" and computer == "Papier") or (user == "Stein" and computer == "Schere") or (user == "Papier" and computer == "Stein"):
        return "The User Won"
    else:
        return "The Computer Won"
    
# functie care face jocul <3 <3 <3
def play_game():
    u_score = 0 
    c_score = 0

    for round_num in range(1, 4): # stabilim numarul de runde fiind 3 
        print(f"Runde {round_num}:") 

        user = alegere_user()
        computer = alegere_calculator()

        print(f"Computerul alege: {computer}")
        result = gaseste_castigator(user, computer)
        print(f"{result} in this round.\n")
        
        if result == "The User Won":
            u_score += 1
        elif result == "The Computer Won":
            c_score += 1

    if u_score < c_score:  # in functie de scorul adunat stabilim castigatorul jocului final 
        print("The Computer is the BOSS!")
    elif c_score < u_score:
        print("The User is the BOSS!")
    else:
        print("NASOL =(")

if __name__ == "__main__":
    play_game()