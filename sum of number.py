a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))

if 1000 <= a <= 9999 and 1000 <= b <= 9999 and 1000 <= c <= 9999:
    a1 = [int(i) for i in str(a)]
    b1 = [int(i) for i in str(b)]
    c1 = [int(i) for i in str(c)]

    large_sum = max(a1) + max(b1) + max(c1)
    small_sum = min(a1) + min(b1) + min(c1)

    key = large_sum * small_sum

    print("Key =", key)
else:
    print("Enter only 4 digit numbers")
