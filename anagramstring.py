from collections import Counter
def is_anagram(s1: str, s2:str)->bool:
    return Counter(s1) == Counter(s2)

#longest palindromic substring 

def longest_Pal_sub(s: str):
    def expand(l,r):
        while l>=0 and r<len(s) and s[l]== s[r]:
            l-=1
            r+=1
        return s[l+1: r]
    longest= ""
    for i in range(len(s)):
        odd = expand(i,i)
        even = expand(i,i+1)
        longest = max(longest, odd, even, key= len)
    return longest 
print(longest_Pal_sub("heelleewo"))
