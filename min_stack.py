class Node:
    def __init__(self, data : int) -> None:
        self.data = data
        self.next = None
        self.prev_min = None


class MinStack:
    def __init__(self):
        self.top = None
        self.min = None
    
    def insert(self, data) -> None:
        if self.top is None:
            self.top = Node(data)
            self.min = self.top
        else:
            temp = self.top
            self.top = Node(data)
            self.top.next = temp

            if data < self.min.data:
                self.top.prev_min = self.min
                self.min = self.top  

    def pop(self):
        if self.top is None:
            return 

        if self.top == self.min:
            self.min = self.top.prev_min
        
        self.top = self.top.next
    

    def get_min(self):
        if self.min:
            return self.min.data

    def __str__(self):
        cur = self.top
        while cur:
            print(cur.data)
            cur = cur.next
        return ''
        
        

min_stack = MinStack()
min_stack.insert(8)
min_stack.insert(9)
min_stack.insert(6)
min_stack.insert(5)
min_stack.insert(18)
min_stack.insert(2)
min_stack.insert(10)
print('minimum of stack is:', min_stack.get_min())
print(min_stack)

min_stack.pop()
print('minimum of stack is:', min_stack.get_min())
print(min_stack)

min_stack.pop()
print('minimum of stack is:', min_stack.get_min())
print(min_stack)
