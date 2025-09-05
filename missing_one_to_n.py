# def findmissing(arr:list[int])->int:
#     n = len(arr) + 1
#     actual_sum = sum(arr)
#     expected_sum = n*(n+1)//2  
#     return expected_sum - actual_sum

# arr = [1,2,3,4,6]
# print(findmissing(arr))


# XOR method 
def find_missing_XOR(arr: list[int])->int:
    n = len(arr)+1
    xor_all = 0
    xor_arr = 0
    for i in range(1 , n+1):
        xor_all^=i
    for j in arr:
        xor_arr^= j
    return xor_all ^ xor_arr
arr = [1,2,3,4,6]
print(find_missing_XOR(arr))

    