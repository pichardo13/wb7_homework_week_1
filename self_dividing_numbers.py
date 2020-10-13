"""
A self-dividing number is a number that is divisible by every digit it contains. 

Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""
def selfDividing(left, right):
    result = []
    for i in range(left, right + 1):
        selfDiv = True
        for j in str(i):
            if j == '0':
                selfDiv = False
            else:
                if i % int(j) != 0:
                    selfDiv = False
                    break

        if selfDiv:
            result.append(i)
    return result

print(selfDividing(1,22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])
