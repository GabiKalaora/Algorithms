class Node:
    def __init__(self, data):
        self.data = data
        self.frequency = 1
        self.right = None
        self.left = None


class MinHeap:
    def __init__(self):
        self.root = None
    

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        
        cur = self.root
        while cur.data <= data and (cur.right is not None and cur.left is not None):
            if cur.data == data:
                cur.frequency += 1
                return

            cur = cur.right if cur.right.data < cur.left.data else cur.left
        
        # cur has one or no children
        if cur.left is None:
            cur.left = new_node
        elif cur.right is None:
            cur.right = new_node

        # cur has both childs and cur.data < data
        else: 
            self.heapify_down(cur, data)
    
    def get_min(self):
        return self.root.data
    
    def heapify_down(self, node, data):
        temp = node.data
        node.data = data

        # node has one or no childre
        if node.left is None:
            node.left = Node(temp)
        elif node.right is None:
            node.right = Node(temp)
        else:
            min_child = node.right if node.right.data < node.left.data else node.left
            self.heapify_down(min_child, temp)

    
    def print_all(self):
        self.print_all_helper(self.root)

    def print_all_helper(self, node):
        if node:
            self.print_all_helper(node.left)
            for i in range(node.frequency):
                print(node.data)
            self.print_all_helper(node.right)



h = MinHeap()
h.insert(15)
h.insert(18)
h.insert(13)
h.insert(14)
h.insert(13)
h.insert(5)
h.insert(7)
h.insert(12)
h.insert(9)



# h.print_all()
print(h.get_min())
    


