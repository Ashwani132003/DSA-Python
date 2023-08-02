class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedlist:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next =  self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node    

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head==None:
            self.head = new_node
        else:
            current_head = self.head
            while current_head.next!=None:
                current_head = current_head.next
            current_head.next = new_node
            new_node.prev = current_head
                
    def insert_after(self, data, prev_node):
        if prev_node is None:
            print('The previous node is not valid')
            return
        new_node = Node(data)
        new_node.next= prev_node.next
        new_node.prev = prev_node

        if prev_node.next:
            prev_node.next.prev = new_node
        prev_node.next=new_node

    def delete(self, key):
        current_head = self.head
        while current_head:
            if current_head.data == key:
                if current_head.prev:
                    current_head.prev.next = current_head.next
                else:
                    self.head = current_head.next

                if current_head.next:
                    current_head.next.prev = current_head.prev
                del current_head
                return
            current_head = current_head.next  
        print('Node with the data/key you gave is not found. ')                  

    def print(self):
        current_head = self.head
        while current_head!=None:
            print(current_head.data, end=" -> ")
            current_head = current_head.next
        print("none")
    def print_backward(self):
        current_head = self.head
        while current_head and current_head.next:
            current_head = current_head.next

        while current_head:
            print(current_head.data, end=" -> ")
            current_head = current_head.prev



        print("none")




l = DLinkedlist()
l.insert_at_start(10)
l.print()
l.insert_at_end(20)
l.print()
l.insert_after(40, l.head.next)
l.print()

l.insert_at_start(60)
l.print()
l.insert_at_start(70)
l.print()

l.insert_at_end(80)
l.print()

l.print_backward()    

l.delete(10)
l.print()

l.delete(100)
l.print()