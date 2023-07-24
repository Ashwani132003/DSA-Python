class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        node=Node(data)   
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node must be valid.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node        
            
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def delete_at_position(self, position):
        if self.head is None:
            return
        current_node = self.head
        if position == 0:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        count = 0
        while current_node and count != position:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None


    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")




l=LinkedList()
l.insert_at_end(50)        
l.insert_at_end(30)          
l.insert_at_end(40)          
l.insert_at_start(1)
l.insert_at_start(2)

l.show()
node_4 = l.head.next.next
l.insert_after(node_4, 17)
l.show()
l.delete_node(1)  # Delete the node with value 1
l.delete_at_position(3) 

l.show()       
