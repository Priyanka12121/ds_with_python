s= raw_input("enter the string")
d={}
c=0
for i in s:
    if i in ['a','e','i','o','u']:
        c=s.count(i)
        d.update({i:c})
print(d)
    
