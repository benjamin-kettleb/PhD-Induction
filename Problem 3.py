def LisOfPrimes(n):
    p = [2]
    maX = int(n**0.5)
    if maX%2 == 0:
        maX+=1
    for i in range(maX,3,-2):
        if isPrime(i):
            isFactor(n,i)
##            p.append(i)
##            print(i)
    return p

def isPrime(num):
    if num % 2 == 0:
        return False
    sqrtNum = int(num**0.5+1)
    for i in range(3,sqrtNum,2):
        if num % i == 0:
            return False
    return True

def isFactor(num,fact):
    if num % fact == 0:
        print(fact)

num = 600851475143

posFacts = LisOfPrimes(num)

##print("worked out primes")
##
##for fac in posFacts:
##    if num % fac == 0:
##        print(fac)
