class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

class doubly_linked:
    def __init__(self):
        self.head = None
        self.size = 0

    def create_doubly_linked(self, string):
        if len(string) == 0 :   return False
        string = list(string)
        self.head = Node(string.pop(0))
        p = self.head
        while len(string) > 0:
            t = Node(string.pop(0))
            p.next = t
            t.prev = p
            p = t

    def print_me(self):
        p = self.head
        s = ""
        while p is not None:
            s = s + p.value
            p = p.next
        print(s, end=" ")
    
    def check_palindrome(self):
        l = r = self.head
        #set the right pointer to the end of the doubly linked list
        while r.next is not None:
            r = r.next
        while l is not None:
            if l.value == r.value:
                if l == r: return True
                l = l.next
                r = r.prev
            else:
                return False

        return True


dl = doubly_linked()
Test_cases = [ "mohom","mangegnam","hooting","t","","90","19091"]
for item in Test_cases:

    if dl.create_doubly_linked(item) == False:
        print(False)
    dl.print_me()
    if dl.check_palindrome() == True:
        print("is a Palindrome")
    else:
        print("Nope")
