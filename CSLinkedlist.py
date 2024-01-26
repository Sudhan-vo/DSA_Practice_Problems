class Node():
    def __init__(self,value):
        self.value=value
        self.next=None

class CSLinkedlist():
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
                r+=str(temp.value)
                temp=temp.next
                if temp==self.head:
                    break
                r+="->"
            return r        
    
    def append(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            newnode.next=newnode
        else:
            self.tail.next=newnode
            newnode.next=self.head
            self.tail=newnode
        self.length+=1    
            
    def prepend(self,value):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
            newnode.next=newnode
        else:
            newnode.next=self.head
            self.head=newnode
            self.tail.next=self.head
        self.length+=1
    
    def insert(self,value,index):
        if index<0 or index>=self.length:
            return None
        elif index==0:
            self.prepend(value)
        elif index==self.length:
            self.append(value)
        else:
            temp=self.head
            newnode=Node(value)
            for _ in range(index-1):
                temp=temp.next
            newnode.next=temp.next
            temp.next=newnode
            self.length+=1
            
    def traverse(self):
        temp=self.head
        while self.head is not None:
            print(temp.value)
            temp=temp.next
            if temp==self.head:
                break
            
    def search(self,value):
        temp=self.head
        i=0
        while self.head is not None:
            if temp.value==value:
                print(f"{value} is in the index {i}")        
            temp=temp.next
            i+=1
            if temp==self.head:
                break
            
    def get(self,index):
        if index<0 or index>=self.length or self.head==None:
            return None
        else:
            temp=self.head
            for _ in range(index):
                temp=temp.next
            return temp
            
    def Set(self,index,value):
        temp=self.get(index)
        if temp: 
            temp.value=value
        
    def pop_first(self):
        temp=self.head
        if self.head==None:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            print(temp.value)
        else:
            self.head=temp.next
            self.tail.next=self.head
            self.length-=1
            print(temp.value)
    
    def pop(self):
        temp=self.head
        if self.head==None:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
            print(temp.value)
        else:
            for _ in range(self.length-1):
                temp=temp.next
            temp.next=self.head
            popped=self.tail
            self.tail=temp
            popped.next=None
            self.length-=1
            print(popped.value)
            
    def Remove(self,index):
        temp=self.head
        if self.head==None:
            return None
        elif index<0 or index>=self.length:
            return None
        elif index==0:
            self.pop_first()
        elif index==(self.length-1):
            self.pop()
        else:
            for _ in range(index-1):
                temp=temp.next
            popped=temp.next
            temp.next=popped.next
            popped.next=None
            self.length-=1
            print(popped.value)
     
    def delete(self):
        if self.length==0:
            return None
        self.tail.next=None
        self.head=None
        self.tail=None
        self.length=0
                       
csl=CSLinkedlist()
csl.append(20)
csl.append(40)
csl.prepend(10)
csl.insert(30,2)
#csl.search(40)
#csl.traverse()
#csl.get(4)
#csl.Set(3, 35)
#csl.pop_first()
#csl.pop()
#csl.Remove(0)
#csl.delete()
print(csl)
print(f"Length of the CSLinked List is {csl.length}")
print(f"Head={csl.head.value}")
print(f"Tail={csl.tail.value}")
