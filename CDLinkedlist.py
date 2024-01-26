class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
        
class CDLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def __str__(self):
        r=""
        temp=self.head
        if self.head==None:
            return"There is no element to print"
        else:
            for _ in range(self.length):
                r+=str(temp.val)
                temp=temp.next
                if temp==self.head:
                    break
                r+="->"
            return r        
    
    def append(self,val):
        new_node=Node(val)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            self.next=new_node
            self.prev=new_node
            self.length=1
        else:
            self.prev=self.tail
            self.tail.next=new_node
            self.tail=new_node
            self.next=self.head
            self.head.prev=new_node
            self.length+=1
        
cdl=CDLinkedlist()
cdl.append(1)
cdl.append(2)
cdl.append(3)
cdl.append(4)
print(cdl)