class Node:
    def __init__(self,data):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def insertion(self,data):
        node=Node(data)       
        if self.head==None:
            node.next=None
            self.head=node
        else:
            node.next=self.head.next
            self.head.next=node

    def prin(self):
        if self.head==None:
            print('Empty')
        temp=self.head
        while temp!=None:

            print(temp.data)
            temp=temp.next


l=LinkedList()
l.insertion(50)        
l.insertion(30)          
l.insertion(40)          

l.prin()       