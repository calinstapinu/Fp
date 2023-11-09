def isprime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nr_mai_mici(num):
    
    prime_nr=[]  # definim o lista goala in care sa bagam numerele prime gasite

    for i in range(2, num): # parcurgem numere de la 2 pana la num
        if isprime(i):      # daca numarul i este prim
            prime_nr.append(i)  # il bagam in acea lista creata folosind ".append(i)"
    return prime_nr #returnam lista cu numerele prime gasite
            
        

result= int(input("Scrie numarul:"))
print(nr_mai_mici(result))