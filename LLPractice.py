class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def isEmpty(self):
        return self.head is None
    def append(self,data):
        newnode= Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            self.tail=newnode
        self.length+=1

    def display(self):
        arr=[]
        curr=self.head
        while curr:
            arr.append(curr.data)
            curr = curr.next
        print("-->".join(map(str,arr)))
    def remove(self,data):
        if self.head is None:
            return

        if self.head.data==data:
            self.head=self.head.next
            return
        curr = self.head
        while(curr.next):
            if curr.next.data==data:
                curr.next=curr.next.next
                return
            curr= curr.next
    def prepend(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

ll=LinkedList()
# ll.append(30)
# ll.append(90)
# ll.append(40)
# ll.append(100)
# ll.display()
# ll.remove(90)
# ll.display()
# print(ll.isEmpty())
while True:
    n=int(input("Enter a number:\n1.append\n2.remove\n3.display\n4.length of LinkedList\n5.Empty?\n6.prepend\n"))
    if n==1:
        appendinput=int(input("Enter Number to append: "))
        ll.append(appendinput)
        ll.display()
    elif n==2:
        removeinput=int(input("Enter number to remove: "))
        ll.remove(removeinput)
        ll.display()
    elif n==3:
        (ll.display())
    elif n==4:
        print(ll.length)
    elif n==5:
        print(ll.isEmpty())
    elif n==6:
        prependinput=int(input("Enter number to prepend:"))
        ll.prepend(prependinput)
        ll.display()

