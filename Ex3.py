sal=int(input('sal ra vared konid:'))
mah=int(input('mah ra vared konid:'))
rooz=int(input('rooz ra vared konid:'))
if sal % 400==0 or (sal %4==0 and sal % 100 !=0):
    list=[31,29,31,30,31,30,31,31,30,31,30,31]
    print(sum(list[:(mah-1)])+rooz)
else:
    list=list=[31,28,31,30,31,30,31,31,30,31,30,31]
    print(sum(list[:(mah-1)])+rooz)
    
        

