class User:
    def __init__(self, per, entl, octn):
        self.per = per
        self.entl = entl
        self.octn = octn
        
    def compare(self, other):
        ret = 0;
        if self.per ==  other.per and self.entl == other.entl:
            ret+=1
            if self.octn == other.octn:
                ret+=1
        return ret

    def __repr__(self):
        return "["+str(self.per)+ ' ' + str(self.entl) + ' ' + str(self.octn)+"]"

class LinkedListIterator:
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            item = self.current
            self.current = self.current.next
            return item

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        out = "["
        if not self.head is None:
            iter = self.head
            while iter:
                out += str(iter.val)
                iter = iter.next
                if (iter):
                    out += "->"
        return out+"]"

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        count = 0
        for i in self:
            count+=1
        return count

    def add(self, num):
        if self.head == None:
            self.head = Node(num)
        elif self.tail == None:
            node = Node(num, self.head, None)
            self.head.next = node
            self.tail = node
        else: 
            node = Node(num, self.tail, None)
            self.tail.next = node
            self.tail = node
    
    def fadd(self, num):
        if self.head == None:
            self.head = Node(num)
        else:
            node = Node(num, None, self.head)
            self.head = node

    def toVector(self, num):
        vec = []
        for i in range(num):
            vec.append(0)
        if not self.head == None:
            iter = self.head
            while iter:
                vec[iter.val.octn-1]+=1
                iter = iter.next
        return vec
class Node:
    def __init__(self, val = None , prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
    