class node:
    def __init__(self,val) -> None:
        self.val=val
        self.next=None

class linkedlist:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def addleft(self,val) -> node:
        n=node(val)
        if self.head is None and self.tail is None:
            self.head=n
            self.tail=n
        else:
            n.next=self.head
            self.head=n
        return n
    
    def addright(self,val) -> node:
        n=node(val)
        if self.head is None and self.tail is None:
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n
        return n
    
    def printlsit(self) -> None:
        if self.head is None and self.tail is None:
            print("list is Empty")
        else:
            p=self.head
            while p is not None:
                print(f"{p.val}")
                p=p.next