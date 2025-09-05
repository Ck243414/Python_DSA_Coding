def rev_string_inplace(s:str)-> str:
    chars = list(s)
    left = 0
    right = len(chars)-1
    while left<right:
        chars[left],chars[right]= chars[right],chars[left]
        left+=1
        right-=1
    return "".join(chars)
test = "hello"
print(test[::-1])
print(rev_string_inplace(test))