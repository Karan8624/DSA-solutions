class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def cycle(list):
    curr = list
    seen = []
    while curr:
        if curr in seen:
            return True
        else:
            seen.append(curr.val)
        curr = curr.next

