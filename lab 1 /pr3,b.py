def isprime(n):
    if n <= 1:                              #daca n este 1 din start spunem ca nu este prim
        return False
    
    if n <= 3:                              #daca n este mai mic egal cu 3 spunem ca este prim deoarece 2 este prim si 3 este prim
        return True
    
    if n % 2 == 0 or n % 3 == 0:             #daca n este divizibil cu 2 sau 3, in caz afirmativ N nu este prim deoarece numerele divizibile cu 2 si 3 nu sunt prime
        return False
    
    i = 5                                    #indexam i cu valoarea 5 deoarece am verificat cazurile precedente 
    while i * i <= n:                        # programul ruleaza pana la radicalul lui N
        if n % i == 0 or n % (i + 2) == 0:   #daca numarul N este divizibi cu i sau i+2, in caz afirmativ returnam False
            return False
        i += 6                               #crestem valoarea lui i cu 6,  (de ce 6?) deoarece precedent am verificat toti multiplii de 2 si 3, 
                                             #deci nu are rost sa o facem din nou
    return True                              #daca cele din if nu au loc, returnam True

""" similiar?
def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
"""

def longest_prim(vector):
    max_l=0                                    #definim 4 contoare
    max_start_ind=-1
    current_l=0
    current_ind=-1

    for i in range(len(vector)):                 # Aceast for parcurge vectorul și verifica pentru fiecare element dacă este prim folosind funcția isprime
        if isprime(vector[i]):
            current_l += 1                       #daca elementul este prim, contorul nostru curent creste
            if current_ind == -1:                #daca indexul contorului este -1 atunci indexul devine pozitia curenta a elementului prim gasit adica i
              current_ind = i
        else:                                    # in cazul in care elementul gasit nu este numar prim verificam daca contorul curent este mai mare decat contorul maxim 
            if current_l > max_l:
                max_l = current_l                # in caz afirmativ, contorul maxim ia valoarea contorului curent
                max_start_ind = current_ind      # si indexul maxim ia valoarea indexului curent i
            current_l = 0                        # la final resetam contoarele curente si bucla se repeta
            current_ind = -1

    if current_l > max_l:
        max_l = current_l
        max_start_ind = current_ind

    if max_start_ind >= 0:                      #verificam daca secventa maxima este mai mare decat 0 , in caz afirmativ returnam secventa 
        return vector[max_start_ind:max_start_ind + max_l]
    else:
        return None                             #in caz negativ returnam None
    

num=input("Introduceti numerele vectorului:")
num_list = [int(x) for x in num.split(",")]
result = longest_prim(num_list)

print(result)

"""   
if longest_prime_sqs:
    print("The longest contiguous prime sequence is:", longest_prime_sqs)
else:
    print("No contiguous prime sequence found.")
"""