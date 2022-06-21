class Queue:
    def __init__(self,max):
        self.l=[]
        self.size=max
        self.front=-1
        self.rear=-1
    def insertion(self,item):
        if self.rear==self.size-1:
            print("Queue is full")
        
        else:
            if self.front==-1:
                self.front=0
            self.rear=self.rear+1
            self.l.append(item)
    def deletion(self):
        if self.front==-1:
            print("Queue is empty")
        else:
            item=self.l[self.front]
            print("Deleting",item)
            
            if self.front==self.rear:
                self.rear=-1
                self.rear=-1
            else:
                self.front+=1
            del(item)
            
    def traverse(self):
        for i in range(self.front,self.rear+1):
            print(self.l[i])
q=Queue(5)
q.insertion(1)
q.insertion(2)
q.insertion(3)
q.insertion(4)
q.insertion(5)
q.deletion()
q.traverse()
