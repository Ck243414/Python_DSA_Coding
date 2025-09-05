def sieve_of_eratosthenes(limit : int) -> list[int]:
    sieve = [True]*(limit+1)
    sieve[0]= sieve[1] = False
    i = 2
    while i*i <=limit:
        if sieve[i]:
            for multiple in range(i*i, limit+1, i):
                sieve[multiple]=False
        i+=1
    primes =[p for p, is_prime in enumerate(sieve) if is_prime]
    return primes

def firstnprimes(n:int)-> list[int]:
    if n<1:
        return[]
    import math
    if n<6:
        limit=15
    else:
        limit = int(n*(math.log(n)+ math.log(math.log(n)))) + 3 

    nprimes = sieve_of_eratosthenes(limit)
    return nprimes[:n]

print(firstnprimes(10))