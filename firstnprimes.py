def isprime(num : int)->bool :
    if num < 1:
        return False
    if num == 2 or num == 3:
        return True
    if num %2 ==0 or num %3 ==0:
        return False
    i = 5
    while i*i <= num:
        if num % i==0 or num% (i+2) ==0:
            return False
        i+=6
    return True 

def nprimes(n:int)-> list:
    primes =[]
    num=2
    while len(primes)<n:
        if isprime(num):
            primes.append(num)
        num+=1
    return primes

firstn = int(input("Enter how many primes to find:"))
print(nprimes(firstn))