class selection:
    def sorting(self):
        self.l=[]
        print("enter the elements:")

        for i in range(0,10):
            t=int(input())
            self.l.append(t)
        for i in range(0,10-1):
            for j in range(i+1,10):
            

                if self.l[i] > self.l[j]:
                    s=self.l[i]
                    self.l[i]=self.l[j]
                    self.l[j]=s
    def display(self):
         for i in range(0,10):
            print(self.l[i],end=",")              
         
def main():
    se=selection()
    se.sorting()
    se.display()
if __name__=="__main__":
    main()
    
    
