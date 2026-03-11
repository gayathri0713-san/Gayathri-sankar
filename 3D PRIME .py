def prime(i):
    if i == 1:
        return False
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c = c + 1
    if c == 0:
        return True
    else:
        return False


def sod(i):
    sum = 0
    while i != 0:
        rem = i % 10
        sum = sum + rem
        i = i // 10
    return sum


def every(i):
    while i != 0:
        d = i % 10 
        if not prime(d):
            return False 
        i = i // 10
    return True

for i in range(100, 1000):
    if prime(i) and prime(sod(i)) and every(i):
        print(i, end=" ")
