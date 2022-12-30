class Node() :
    def __init__(self, value=None) -> None:
        self.value = value
        self.next  = None


class SingleLinkedList() :
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __iter__(self) :
        node = self.head
        while node :
            yield node
            node = node.next
            
    def __str__(self) :
        values = [str(node.value) for node in self]
        return ' -> '.join(values)

    def __len__(self) :
        node = self.head
        cnt = 0
        while node :
            cnt += 1
            node = node.next
        return cnt

    def insert(self, value, location) -> None :
        newNode = Node(value)
        if self.head is None :  # Empty linked list
            self.head = newNode
            self.tail = newNode
        else :                  # Non empty linked list
            if location == 0 :
                newNode.next = self.head
                self.head = newNode

            elif location == -1 :
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else :
                tempNode = self.head
                idx = 0
                while idx < location -1 :
                    tempNode = tempNode.next
                    idx += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def traverse(self) -> None :
        if self.head == None :
            print("Linkedlist does not exist")
        
        else :
            node = self.head
            while node is not None :
                print(node.value)
                node = node.next

    def search(self, value_to_search) :
        if self.head == None:
            print("Linked list does not exist")
        else :
            node = self.head
            idx = 0
            while node is not None:
                if node.value == value_to_search :
                    return idx
                node = node.next
                idx += 1
            return -1

    def delete(self, location) :
        assert location < len(self), f"index {location} out of range {[0, len(self)]}"
        if self.head == None :
            print("Linked list does not exist")

        else :
            if location == 0 :
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else :
                    self.head = self.head.next

            elif location == -1 :
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else :
                    node = self.head
                    while node is not None and node.next != self.tail :
                        node = node.next
                    node.next = None

            else :
                node = self.head
                idx = 0
                while idx < location -1 :
                    node = node.next
                    idx += 1
                node.next = node.next.next
                
    def deleteEntireList(self) :
        if self.head == None :
            print("Linked list does not exist")
        else :
            self.head = None
            self.tail = None


class CircularLinkedList () :
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) :
        node = self.head 
        while node :
            yield node
            node = node.next
            if node == self.tail.next :
                break

    def __len__(self) :
        node = self.head
        cnt = 0
        while node :
            cnt += 1
            node = node.next
            if node == self.head :
                return cnt

    def insert(self, value, location) :
        newNode = Node(value)

        if self.head == None :  # Empty linked list
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        
        else :                  # Non empty linked list
            if location == 0 :
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode

            elif location == -1 :
                self.tail.next = newNode
                self.tail = newNode
                newNode.next = self.head 

            else :
                node = self.head
                idx = 0
                while idx < location -1 :
                    idx += 1
                    node = node.next
                newNode.next = node.next
                node.next = newNode

    def traverse(self) :
        if self.head == None :
            print("Linked list does not exist")
        else :
            node = self.head 
            while node :
                print(node.value)
                node = node.next
                if node == self.head :
                    break

    def search(self, value_to_search) :
        if self.head is None :
            print("Linked list does not exist")
        
        else :
            node = self.head 
            idx = 0
            while node :
                if node.value == value_to_search:
                    return idx
                else :
                    node = node.next
                    idx += 1
                    if node == self.head :
                        return -1

    def delete(self, location) :
        if self.head is None :
            print("Linked list does not exist")
        else :
            if location == 0:
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else :
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == -1 :
                if self.head == self.tail :
                    self.head = None
                    self.tail = None
                else :
                    node = self.head 
                    while node.next != self.tail :
                        node = node.next
                    node.next = self.head
                    self.tail = node

            else :
                assert location <= len(self), "index out of range"
                node = self.head 
                idx = 0
                while idx < location -1 :
                    node = node.next
                    idx += 1
                node.next = node.next.next
            
    def deleteEntireList(self) :
        if self.head is None :
            print("Linked list already does not exist")
        else :
            self.head = None
            self.tail.next = None
            self.tail = None