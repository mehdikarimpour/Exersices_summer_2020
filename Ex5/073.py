f1=input('food1:')
f2=input('food2:')
f3=input('food3:')
f4=input('food4:')
d1={1:f1,2:f2,3:f3,4:f4}
print(d1)
r=int(input('Wich number you want to remove?:'))
d1.pop(r)
print(d1)
