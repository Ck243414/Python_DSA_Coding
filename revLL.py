class ListNode:
    def __init__(self,val = 0, next=None):
        self.val = val 
        self.next = next
    
def iterative_revLL(head : ListNode)->ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next 
        curr.next = prev
        prev = curr
        curr = nxt 
    return prev
def printList(head:ListNode):
    while head:
        print(head.val, end= " -> ")
        head = head.next
    print("None")

def recursive_revLL(head: ListNode) ->ListNode:
    if not head or not head.next:
        return head
    new_head = recursive_revLL(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    printList(node1)
    newhead = recursive_revLL(node1)
    printList(newhead)
