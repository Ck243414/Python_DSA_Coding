# def max_sum_subarray(nums: list[int])->int:
#     if not nums:
#         return 0
#     max_sum = current_sum = nums[0]
#     for i in range(1, len(nums)):
#         current_sum = max(nums[i], current_sum+ nums[i])
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  
# print(max_sum_subarray(arr))

def max_sum(arr: list[int])-> tuple[int, list[int]]:
    if not arr:
        return 0, []
    max_sum = current_sum = arr[0]
    start = end = 0
    temp_start = 0
    for i in range(1, len(arr)):
        if arr[i]> current_sum + arr[i]:
            current_sum= arr[i]
            temp_start = i
        else:
            current_sum+=arr[i]
        if current_sum> max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    return max_sum , arr[start:end+1]

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  
print(max_sum(arr))

