def __init__(self):
    self.stack = []
    self.minstack = [float('inf')]

    

def push(self, value):
    """
    :type value: int
    :rtype: None
    """ 
    self.stack.append(value)
    self.minstack.append(min(value,self.minstack[-1]))
    

    

def pop(self):
    """
    :rtype: None
    """
    self.stack.pop()
    self.minstack.pop()

    

def top(self):
    """
    :rtype: int
    """
    return self.stack[-1]

def getMin(self):
    """
    :rtype: int
    """
    return self.minstack[-1]
