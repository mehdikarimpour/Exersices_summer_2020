def fibo(arg):
        if arg<=0:
                print("error")
        elif arg==1 or arg==2:
                return 1
        else:
                return fibo(arg-1)+fibo(arg-2)
def list_fibo(arg):
        if arg<=0:
                print('error')
        elif arg==1:
                return [0]
        elif arg==2:
                return [0,1]
        else:
                while arg==2:
                        return [fibo(arg)]
n=int(input("Enter your number:"))
print(fibo(n))
print(fibo(arg))
