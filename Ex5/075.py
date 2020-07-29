l1=['000','100','110','111']
print(l1)
i=0
a=input('Enter your digit number:')
while i<=3 and i>=0:
    if a==l1[i]:
        b=l1.index(a)
        print(b)
        i=5
    i+=1
    if i==4:
        print("that is not in the list")
        
    
    
