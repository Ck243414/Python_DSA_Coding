
def lcs_memo(s1 : str, s2:str)->int:
    from functools import lru_cache
    @lru_cache(None)
    def solve(i : int, j : int):
        if i==0 or j==0:
            return 0
        if s1[i-1] == s2[j-1]:
            return 1 + solve(i-1, j-1)
        else:
            return max(solve(i-1,j), solve(i,j-1))
    return solve(len(s1),len(s2))
print(lcs_memo("abcde","abde"))