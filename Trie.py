class Node:
    def __init__(self, letter) -> None:
        self.char = letter
        self.children = dict()
        self.end_word = False



class Trie:
    def __init__(self) -> None:
        self.head = Node('')

    
    def insert(self, word) -> None:
        cur = self.head
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                new_node = Node(char)
                cur.children[char] = new_node
                cur = new_node
        cur.end_word = True


    def delete(self, word) -> None:
        cur = self.head
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return 
        cur.end_word = False


    def print_all(self) -> None:
        return self.print_all_helper('', self.head)


    def print_all_helper(self, string, node):
        if node.end_word:
            print(string)
        for char in node.children:
            self.print_all_helper(string + char , node.children[char]) 
    

    def prefix(self, prefix):
        cur = self.head
        for char in prefix:
            cur = cur.children[char]
        self.print_all_helper(prefix, cur)
    
    

d = Trie()
d.insert('cars')
d.insert('python')
d.insert('catf')
d.insert('cat')
# d.delete('python')

d.print_all()
d.prefix('ca')








    






