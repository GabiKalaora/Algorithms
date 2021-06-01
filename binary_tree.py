class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.__len = 0

    def insert(self, data):
        self.root = self.__insert_helper(self.root, data)

    def __insert_helper(self, node, data):
        if node is None:
            self.__len += 1
            return Node(data)
        else:
            if data < node.data:
                node.left = self.__insert_helper(node.left, data)
            elif data > node.data:
                node.right = self.__insert_helper(node.right, data)
            else:
                print('data already in tree')
        return node

    def __str__(self):
        res = []
        res = self.__str_helper(self.root, res)
        return str(res)

    def __str_helper(self, node, lst_data):
        if node:
            self.__str_helper(node.left, lst_data)
            lst_data.append(node.data)
            self.__str_helper(node.right, lst_data)
        return lst_data

    def __len__(self):
        return self.__len

    def print_all(self):
        self.__print_all_helper(self.root)

    def __print_all_helper(self, node):
        if node:
            self.__print_all_helper(node.left)
            print(node.data)
            self.__print_all_helper(node.right)

    def search(self, data):
        return self.__search(self.root, data)

    def __search(self, node, data):
        if node:
            if node.data == data:
                return node
            elif data < node.data:
                return self.__search(node.left, data)
            elif data > node.data:
                return self.__search(node.right, data)
        else:
            return None

    def is_leaf(self, node):
        if node.right is None and node.left is None:
            return True
        return False

    def get_min(self, node):
        # if node.left:
        #     return self.get_min(node.left)
        # else:
        #     return node
        cur = node
        while cur:
            if cur.left:
                cur = cur.left
            else:
                return cur

    def successor(self, node):
        # first case: node has right child so successor is most left child in this right subtree
        if node.right:
            return self.get_min(node.right)

        # second case: if no right child successor is ancestor that has a left child that is also ancestor of node
        succ = None
        cur = self.root
        while cur:
            if cur.data > node.data:
                succ = cur
                cur = cur.left
            elif cur.data < node.data:
                cur = cur.right
            else:
                break
        return succ

    def delete(self, data):
        return self.__delete(self.root, data)

    def __delete(self, node, data):
        if node is None:
            return node

        # get node to delete
        if data < node.data:
            node.left = self.__delete(node.left, data)
        elif data > node.data:
            node.right = self.__delete(node.right, data)

        # we holding node to delete
        else:
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                succ = self.successor(node)
                succ.right = self.__delete(succ.right, succ.data)
            self.__len -= 1
        return node


bst = BST()
bst.insert(10)
bst.insert(7)
bst.insert(12)
bst.insert(1)
bst.insert(8)
bst.insert(11)
bst.insert(15)
bst.insert(14)
print(bst)
print('len ->', len(bst))
bst.delete(8)
print(bst)
print('len ->', len(bst))
print(bst.get_min(bst.root).data)
