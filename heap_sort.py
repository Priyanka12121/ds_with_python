class heap_sort:
    def heapify(list,i,n):
        
        l=2*i+1
        r=2*i+2
        lar=i
        if r<n and list[r]>list[lar]:
            lar=r
        if l>n and list[l]>list[lar]:
            lar=l
        if lar==i:
            return
        else:
            t=list[lar]
            list[lar]=list[i]
            list[i]=t
            heapify(list,lar,n)
    def heap(list,n):
        for i in range(n//2,-1,-1):
            heapify(list,i,n)
        for i in range(n-1,0,-1):
            list[i],list[0]=list[0],list[i]
            heapify(list,i,0)
    def display():
        print(list)
h=heap_sort
list=[30,25,60,71,35,48,80,55,20,38]
h.heap(list,10)
h.display()
