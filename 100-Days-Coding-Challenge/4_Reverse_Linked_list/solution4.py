class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0

    def creat_linked_list(self, string):
        self.head = Node(string[0])
        p = self.head
        for i in range(1, len(string)):
            t = Node(string[i])
            p.next = t
            p = t

    def print_list(self):
        p =self.head
        while p is not None:
            print(p.data,end="")
            p = p.next

    def reverse_list_by_word(self):
        string = ""
        p = self.head
        while p is not None:
            string = string+p.data
            p = p.next
        words = string.split(" ")

        result = []
        for word in words:
            s = list(word)
            s.reverse()
            s = "".join(s)
            result.append(s)
        return " ".join(result)

l = Linked_List()
test_string = "Hello World"
l.creat_linked_list(test_string)
print("Before : ",test_string)
print("After : ",l.reverse_list_by_word())
