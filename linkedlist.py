class node:
    def __init__(self,item):
            self.info=item
            self.link=None
class linkedlist:
        def __init__(self,item):
            self.start=node(item)
            
        def insert_at_last(self,item):
            n=node(item)
            t=self.start
            while t.link!=None:
                    t=t.link
            t.link=n
        def insert_at_begin(self,item):
            n=node(item)
            n.link=self.start
            self.start=n
        def insert_at_specific(self,item,pos):
            n=node(item)
            t=self.start
            p=1
            while(t!=None and p<pos):
                prev=t
                t=t.link
                p=p+1
            prev.link=n
            n.link=t
            
        def traverse(self):
            t=self.start
            while t!=None:
                print(t.info)
                t=t.link
        def delete_at_last(self):
            t=self.start
            while(t.link!=None):
                prev=t
                t=t.link
            print("deleting at last ",t.info)
            del(t)
            prev.link=None
        def delete_at_begin(self):
            t=self.start
            self.start=t.link
            print("deleting at begin ",t.info )
            del(t)
        def delete_at_specific(self,pos):
            t=self.start
            p=1
            while(t!=None and p<pos):
                prev=t
                t=t.link
                p=p+1
            print("deleting at specific",t.info)
            prev.link=t.link
            del(t)
            
            
l=linkedlist(30)
l.insert_at_begin(10)
l.insert_at_last(20)
l.insert_at_last(40)
l.insert_at_begin(5)
l.insert_at_specific(60,3)
l.delete_at_last()
l.delete_at_begin()
l.delete_at_specific(3)
l.traverse()

            
