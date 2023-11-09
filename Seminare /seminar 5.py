# 1

def find_perfect(matrix):

    for i in range(len(matrix)):
        sum_line = 0    
        for j in range(len(matrix)):
            sum_line += matrix[i][j]

            if sum_line == numar_perf():
                return True

def numar_perf(x):
    sum = 0
    for i in range(1, x//2+1):
        if x%i == 0:
            sum+=i
    if sum == x:
        return True
    else:
        return False
        

def test_find_perfect():
    assert find_perfect('') == 


# 2
def sum_diag(matrix):
    result = []
    for i in range(len(matrix)):
        sum_line=0
        for j in range(len(matrix)):
            if i!=j:
                sum_line += matrix[i][j]

            result.append(sum_line == matrix[i][j])
            # if sum_line == matrix[i][i]:
            #     result.append(True)
            # else:
            #     result.append(False)





# 4
def longest_word(file):
    f = open(filename, 'r')
    result = []

    for line in r:
        words = line.split(' ')
        
        max_l = 0
        for word in words:
            word = word.strip() 
            if len(word) > max_l:
                max_l = len(word)

        result.append(max_l)


    f.close()
    return result




# 5 
def count_pali(filename):
    f = open(filename, 'r')
    result = []

    for line in f:
        words = line.split(' ')

        for word in words:
            word = word.strip()

            if word == word[::-1]:
                if word in result:
                    result[word] +=1
                else:
                    result[word] = 1




# test 1
def test_sum_diag():
    assert sum_diat(
        [4,3,1],
        [1,2,1],
        [0,5,1]
    ) == [True, True, False]

# test 2
def test_longest_word():
    assert longest_word('test.input') == [4, 5]

# test 3
def test__countpali():
    assert count_pali('test2.input') == {'anna': 2, 'abba': 2}


# apeluri 
test_longest_word()
test_sum_diag()
test__countpali()


def main():
    pass