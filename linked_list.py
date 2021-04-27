class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur:
                if cur.next is None:
                    cur.next = Node(data)
                    break
                else:
                    cur = cur.next

    def delete(self, data):
        if self.head.data == data:
            self.head = self.head.next
        cur = self.head
        while cur:
            if cur.next:
                if cur.next.data == data:
                    cur.next = cur.next.next
            cur = cur.next

    def search(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next

    def sort(self):
        linked_list = LinkedList()
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next
        res = sorted(res)
        cur = self.head
        for item in res:
            cur.data = item
            cur = cur.next

        return linked_list

    def __str__(self):
        res = []
        cur = self.head
        while cur:
            res.append(cur.data)
            cur = cur.next
        return str(res)


def find_cycle(node):
    hash_table = dict()
    cur = node
    while cur:
        if cur not in hash_table:
            hash_table[cur] = True
            cur = cur.next
        else:
            return cur


def get_intersection(head_a, head_b):
    len_a, len_b = 0, 0
    cur_a, cur_b = head_a, head_b

    while cur_a:
        len_a += 1
        cur_a = cur_a.next

    while cur_b:
        len_b += 1
        cur_b = cur_b.next

    cur_a, cur_b = head_a, head_b
    for i in range(abs(len_a - len_b)):
        if len_a > len_b:
            cur_a = cur_a.next
        elif len_b > len_a:
            cur_b = cur_b.next

    while cur_a:
        if cur_a == cur_b:
            return cur_a
        else:
            cur_a = cur_a.next
            cur_b = cur_b.next


d = LinkedList()
for i in range(1, 6):
    d.insert_end(i)
for j in range(6, 11):
    d.insert_beg(j)
print(d)
d.sort()
print(d)
d.delete(3)
d.delete(1)
d.delete(9)
d.delete(10)
print(d)
