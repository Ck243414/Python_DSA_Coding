#finding duplicates by floyds Tortoise-Hare problem 

# def find_duplicates(nums : list[int])->int:
#     n= len(nums)-1
#     for num in nums:
#         if num<1 or num> n:
#             raise ValueError("Invalid Input")
#     slow = nums[0]
#     fast = nums[0]
#     while True:
#         slow = nums[slow]
#         fast = nums[nums[fast]]
#         if slow == fast:
#             break

#     slow = nums[0]
#     while slow != fast:
#         slow = nums[slow]
#         fast = nums[fast]
#     return slow 

# arr = [3, 1, 4 ,2 ,3]
# print(find_duplicates(arr))



# finding duplicates by sorting - O(nlogn)
# def find_duplicates(nums:list[int])->int:
#     nums.sort()
#     for i in range(1,len(nums)):
#         if nums[i]== nums[i-1]:
#             return nums[i]
#     return -1

# arr = [3, 1, 4 ,2 ,3]
# print(find_duplicates(arr))



#finding duplicates by hash set 

def find_duplicates(nums:list[int])->int:
    seen = set()
    for i in nums:
        if i in seen:
            return i
        seen.add(i)
    return -1

arr = [3, 1, 4 ,2 ,3]
print(find_duplicates(arr))




