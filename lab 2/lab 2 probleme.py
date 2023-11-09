
# a)

def elim_duplicates(numere):
    new_num = []                    # noua lista cu numere care nu se repeta
    for nr in numere:               # luam fiecare numar din lista initiala si il bagam in lista noua cat timp nu a mai fost bagat
        if nr not in new_num:
            new_num.append(nr)     
    return new_num


# b)

def inversare_nr(num):
    num = str(num)

    num_inv_str = num[::-1]

    num_inv = int(num_inv_str)
    return num_inv

#def inversare_nr_babeste(num):
    inversul = (num % 10) * 10 + num //10
    for nr in numere:
        invers = inversare_nr_babeste(nr)


def nr_simetrice(numere):
    cnt = 0
    for nr in numere:
        invers = inversare_nr(nr)
        if invers in numere and invers != nr:
            cnt += 1
    return cnt//2

# c)

# "11", "11", "33", "33", "31", "71"  ->  713333311111

def max_concatenare(numere):
    numar_max = 0

    lista_noua = sorted(numere, reverse=True)    # inversam lista de numere

    for num in lista_noua:                       #transformam lista intr un numar intreg
        numar_max = numar_max * 100 + num
    return numar_max
    
# d)

def xor_encrypt(numbers):
    key = int(numbers[0])
    encrypted_num = [(int(num) * key) for num in numbers]
    encrypted_num = [(int(num) + key) for num in numbers]
    encrypted_num = [(int(num) ^ key) for num in numbers]

    return encrypted_num

# e)

# "11", "11", "33", "33", "31", "71"

def filtare_num(numere, expresie):
    lista_filtrate = []
    for nr in numere:   
        x=nr//10
        y=nr%10
        if eval(expresie):
            lista_filtrate.append(nr)
    return lista_filtrate

# f)

def domino(numar1, numar2):  
    return numar1 % 10 == numar2 // 10 or numar1 // 10 == numar2 %10

def secventa_maxima(numere):
    max_l = 1
    max_start_ind = 0
    current_l = 1
    current_ind = 0

    for i in range(1, len(numere)):
        if domino(numere[i - 1], numere[i]):
            current_l += 1
        else:
            if current_l > max_l:
                max_l = current_l
                max_start_ind = current_ind
            current_l = 1
            current_ind = i

    if current_l > max_l:
        max_l = current_l
        max_start_ind = current_ind

    if max_l > 1:
        return numere[max_start_ind:max_start_ind + max_l]
    else:
        return None           

# g)

def cmmdc(a,b):
    while (a!=b):
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def cmmmc(a,b):
    return a * b 

def gaseste(l,a,b):
    return cmmmc(l[a],l[b])

#Exemple
numbers_list0 = [31, 28, 11, 82, 91, 82, 42, 24]
numbers_list = [11, 11, 33, 13, 63,33, 31, 71, 62]
numbers_list2 = [85, 59, 91, 12, 32, 26, 91]

print("\n")
print(elim_duplicates(numbers_list))
print("\n")
print(nr_simetrice(numbers_list0)) 
print("\n")
print(max_concatenare(numbers_list)) 
print("\n")
print("XOR Encryption =", xor_encrypt(numbers_list))
print("\n")
print("Numerele care indeplinesc conditia =", filtare_num(numbers_list, "x==y*2"))
print("\n")
print("Secventa maxima domino =", secventa_maxima(numbers_list2))
print("\n")
print(gaseste([5,6,3,12,24,48],3,5))
print()
