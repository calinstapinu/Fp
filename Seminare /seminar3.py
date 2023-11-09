def find_str(target, source):
    for i in range(len(target)- len(source) + 1):
        cnt=0
        j=i
        for idx in range(len(source)):
            if target[j] == source[idx]:
                cnt+=1
            j+=1
        if cnt == len(source):
            return i
    return -1



def find_str_better(target, source):
    for i in range(len(target)- len(source) + 1):
        if target[i:i+len(source)] == source:
            return i 
    return -1



def find_str_even_better(target, source):
    position = -1
    j = 0 # index for source

    for i in range(len(target)):
        if target [i] != source[j]:
            j=0
            position = -1
        if target[i] == target[j]:
            if j ==0:
                position = i 
        
        if j>= len(source) -1:
            break
        else:
            j+=1
    return -1





def test_find_str_better():
    assert find_str('string', 'ing') == 3
    assert find_str('string', 'ffr') == -1

def test_find_str():
    assert find_str_better('string', 'ing') == 3
    assert find_str_better('string', 'ffr') == -1

def test_find_str_even_better():
    assert find_str_even_better('string', 'ing') == 3
    assert find_str_even_better('stiring', 'ing') == 4
    assert find_str_even_better('string', 'ffr') == -1







# pr 1

def find_sum(numbers, sum):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j] == sum:
                return True

    return False


def test_find_sum():
    assert find_sum([1,2,9],3) == True
    assert find_sum([1,2,9],12) == False


# pr 2
def generate_multiple(number, count):
    multi = [number]

    for i in range(2, count+1):
        multi.append(number*i)

    return multi

def test_generate_multiple():
    assert generate_multiple(3, 4) == [3, 6, 9, 12]
    assert generate_multiple(2, 2) == [2, 4]


# pr 3

# def big_sum(a, b):
#     s = 0  
#     t = 0
#     p = 1

#     for i in range(len(a)-1, -1, -1):
#         sum = int(a[i]) + int(b[i]) + t 


#         if sum > 9:
#             t=1
#         else:
#             t=0


#         s = (sum%10)*p
#         p *+ 10
    
#     if t == 1:
#         s = p + s

#     return str(s)


# def test_big_sum():
#     assert big_sum('123' , '123') =='246'
#     assert big_sum('123' , '129') =='252'
#     assert big_sum('999' , '101') =='1100'



# pr 4


def reverse(word):
    vok = 'aeiou'
    vok_in_word=[]
    new_word = ''

    for ch in word:
        if ch in vok:
            vok_in_word.append(ch)
    i=1
    for ch in word:
        if ch not in vok:
            new_word += ch
        else:
            new_word += vok_in_word[-i]
            i+=1

    return new_word



def test_reverse():
    assert reverse('Terminator') == "Tormaniter"

# pr 6
def big_sum_pr6(a, b):
    s = 0  
    t = 0
    p = 1
    
    if a > b:
        x = len(a) - len(b)
        b = '0'*x+b
    else:
        x = len(b) - len(a)
        a = '0'*x+a

    for i in range(len(a)-1, -1, -1):
        sum = int(a[i]) + int(b[i]) + t 


        if sum > 9:
            t=1
        else:
            t=0


        s = (sum%10)*p
        p *+ 10
    
    if t == 1:
        s = p + s

    return str(s)


def test_big_sum_pr6():
    assert big_sum_pr6('123' , '123') =='246'
    




test_generate_multiple()
test_find_sum()
test_find_sum()
test_find_str()
test_find_str_better()
#test_big_sum()
test_big_sum_pr6()
test_reverse()
def main():
    pass