class array1:
    def __init__(self,s):
        self.size=s
        self.l=[]
    def create_array(self):
        print("enter the elements of list")
        for i in range(0,self.size):
            t=int(input())
            self.l.append(t)
            
    def show_array(self):
        print(self.size)
        print(self.l)
    def linear_search(self,n):
        f=0
        for i in self.l:
            if i==n:
                print("found")
                f=1
                break
        if(f==0):
            print("not found")
    def sorting(self):
        self.l.sort()
        print(self.l)
    def binary_search(self,x):
        lo=0
        h=self.size-1
        f=0
        while lo<=h:
            m=(lo+h)/2
            print(m,self.l[m])
            if self.l[m]==x:
                f=1
                break
            elif self.l[m]>x:
                h=m-1
            elif self.l[m]<x:
                lo=m+1
        if f==1:
            print("found at position",m)
        else:
            print("not found" )
def main():
    a=array1(5)
    a.create_array()
    a.show_array()
    a.linear_search(2)
    a.sorting()
    a.binary_search(5)
if __name__=='__main__':
    main()

    
            
                
        
    
