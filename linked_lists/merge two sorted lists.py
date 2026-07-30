class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def merge(list1,list2):
    dummy  = ListNode(0)
    curr = dummy
    curr1 = list1
    curr2  = list2
    while curr1 and curr2:
        if curr1.val >= curr2.val:
            curr.next = curr2
            curr2 = curr2.next
        else:
            curr.next = curr1
            curr1 = curr1.next
        curr = curr.next

    curr.next = curr1 or curr2

    return dummy.next
"""
list1: 1 → 2 → 4
list2: 1 → 3 → 4"""
# Create list1: 1 → 2 → 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Create list2: 1 → 3 → 4
list2 = ListNode(1)
list2.next = ListNode(3)

# Run and print result
result = merge(list1, list2)
while result:
    print(result.val, end=" → ")
    result = result.next