class time:
#tarif kardane tavabe baraye class-------------------------------------------------
    def __init__(self,h,min,sec):
        self.h=h
        self.min=min
        self.sec=sec
    def show(self):
        return str(self.h)+':'+(self.min)+':'+(self.sec)
    def __str__(self):
        return str(self.h)+':'+str(self.min)+':'+str(self.sec)
    def __repr__(self):
        return str(self.h)+':'+str(self.min)+':'+str(self.sec)


    def __add__(self,other):
         
        a=self.h+other.h
        b=self.min+other.min
        c=self.sec+other.sec
        if c >=60:
            b=b+1
            c=c-60
        if b >=60:
            a=a+1
            b=b-60
        if a>=24:
            c=c+1
            a=a-25
        return(a,b,c)
       
    def __gt__(self,other):
        total1=self.sec+self.min*60+self.h*3600
        total2=other.sec+other.min*60+other.h*3600
        if total1>total2:
            return self
        elif total1==total2:
            return 'barbar hastand'
        else:
            return other

    def __sub__(self,other):
        return self.h-other.h,self.min-other.min,self.sec-other.sec
#Main--------------------------------------------------------------------------        
t1=time(6,59,59)
t2=time(5,3,4)
print(t1)
print(t2)
print(t1+t2)
print('bozorgat:',t1>t2,' hastesh')
print(t1-t2)

