def naive_fib_recursion(n: int)->int:
    if n<=1:
        return 1
    return naive_fib_recursion(n-1) + naive_fib_recursion(n-2)

def fib_memo(n:int, memo ={})->int:
    if n in memo:
        return memo[n]
    if n <=1 :
        memo[n]= n
    else:
        memo[n]= fib_memo(n-1, memo) +fib_memo(n-2, memo)
    return memo[n]

def fib_tabulation(n: int) -> int:
    if n<=1:
        return n
    dp = [0]* (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(naive_fib_recursion(6))
print(fib_memo(6))
print(fib_tabulation(6))