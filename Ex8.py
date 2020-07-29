def day_of_year(rooz,mah,sal):
   
    if sal % 400==0 or (sal %4==0 and sal % 100 !=0):
        return 'kabise hast'
    else:
        return 'kabise nist'


sal=int(input('sal ra vared konid:'))
mah=int(input('mah ra vared konid:'))
rooz=int(input('rooz ra vared konid:'))
if day_of_year(rooz,mah,sal)=='kabise hast':
    l=[31,29,31,30,31,30,31,31,30,31,30,31]
    print((sum(l[:(mah-1)])+rooz))
if day_of_year(rooz,mah,sal)=='kabise nist':
    l=[31,28,31,30,31,30,31,31,30,31,30,31]
    print((sum(l[:(mah-1)])+rooz))
