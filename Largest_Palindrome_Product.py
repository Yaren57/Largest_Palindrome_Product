def Palindrome(num):
    return str(num) == str(num)[::-1]
def buyuk(min, max):
    a = 0
    for x in range(max, min, -1):
        for y in range(max,min, -1):
            if Palindrome(x*y):
                if x * y > a:
                    a = x * y
    return a
print (buyuk(100,999))
