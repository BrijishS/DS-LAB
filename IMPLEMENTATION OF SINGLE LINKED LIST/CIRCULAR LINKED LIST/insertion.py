class Node:
    def__init_(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def addToEmpty(self,data):
        if self.last!=None:
            return self.last
        temp=Node(data)
        self.last=temp
        self.last.next=self.last
        return self.last
    def addBegin(self,data):
        if (self.last==None):
            return self.addToEmpty(data)
        temp=Node(data)
        temp.next=self.last.next
        self.last.next=temp
        return self.last
    def addEnd(self,data):
        if(self.last==None):
            return self.addToEmpty(data)
        temp=Node(data)
        temp.next=self.last.next
        
