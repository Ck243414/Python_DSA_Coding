# class Node:
#     def __init__(self,val):
#         self.val = val 
#         self.next = None 
    
# def revLL(head):
#     prev = None
#     curr = head
#     while curr:
#         nxt = curr.next
#         curr.next = prev
#         prev = curr
#         curr = nxt
#     return prev 


# def spiralMatrix(matrix):
#     res = []
#     while matrix:
#         res += matrix.pop(0)
#         if matrix and matrix[0]:
#             for row in matrix:
#                 res.append(row.pop())
#         if matrix:
#             res += matrix.pop()[::-1]
#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 res.append(row.pop(0))
#     return res
# mat = [[1,2,3],[4,5,6],[7,8,9]]
# print(spiralMatrix(mat))

def iterativedfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(reversed(graph[node]))

print("\nDFS (iterative): ", end="")
 
