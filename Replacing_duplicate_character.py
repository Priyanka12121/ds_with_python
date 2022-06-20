s=raw_input("enter the string")
wd=""
for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            wd=wd+s[i]
        else:
            wd=wd+"*"
print(wd)
