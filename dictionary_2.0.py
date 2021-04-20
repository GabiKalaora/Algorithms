class Node:
    def __init__(self, char=''):
        self.letter = char
        self.children = dict()
        self.end_word = False

    def __str__(self):
        return '{}'.format(self.letter)


class Dictionary:
    def __init__(self):
        self.base = Node()

    def insert(self, word):
        node = self.base
        for i, letter in enumerate(word):
            if letter not in node.children:
                prefix = word[:i + 1]
                node.children[letter] = Node(prefix)
            node = node.children[letter]
        node.end_word = True

    def delete(self, word):
        node = self.base
        for i, letter in enumerate(word):
            if letter in node.children:
                node = node.children[letter]
        node.end_word = False

    def __print_all_helper(self, node):
        if node.end_word:
            print(node)
        for letter in node.children:
            self.__print_all_helper(node.children[letter])

    def print_all(self):
        self.__print_all_helper(self.base)

    def __prefix_helper(self, node, words_lst):
        if node.end_word:
            words_lst.append(node.letter)
        for letter in node.children:
            self.__prefix_helper(node.children[letter], words_lst)

    def prefix(self, prefix):
        node = self.base
        all_words_prefix = []
        for letter in prefix:
            if letter not in node.children:
                return all_words_prefix
            node = node.children[letter]
        self.__prefix_helper(node, all_words_prefix)
        return all_words_prefix


d = Dictionary()
d.insert('apple')
d.insert('applebee')
d.insert('app')
d.insert('abs')
d.insert('absolutely')
d.insert('python')
d.insert('payment')
d.insert('paypal')
d.insert('payment')
d.print_all()
print(d.prefix('ap'))
d.delete('applebee')
d.delete('paypal')
print(d.prefix('ap'))
print(d.prefix(''))
d.print_all()
