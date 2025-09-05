class ListNode:
    def __init__(self, val= 0, next=None):
        self.val = val 
        self.next = next

# def has_cycle(head: ListNode) ->bool:
#     if not head or not head.next:
#         return False
#     slow = head
#     fast = head.next
#     while slow != fast:
#         if not fast or not fast.next:
#             return False
#         slow = slow.next 
#         fast = fast.next.next
#     return True

def detect_cycle(head: ListNode)-> ListNode:
    if not head or not head.next:
        return None
    slow = head
    fast = head
    while fast or fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    slow = head
    while slow != fast:
        slow = slow.next 
        fast = fast.next 
    return slow 


if __name__ =="__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    cycle_start = detect_cycle(node1)
    if cycle_start:
        print("Cycle starts at node:", cycle_start.val)
    else:
        print("There is no cycle")
