a=int(input())
b=int(input())
tolerans=float(input())


def f(x):
    
    return x**3 - x**2 + 2



def find_root(a,b,tolerance):
    
    
   
    
    while (b-a)>=tolerance:
        c=(a+b)/2
        
        if f(c)==0:
            break
        
        if f(a)*f(c)<0:
            b=c
        if f(b)*f(c)<0:
            a=c
    return f"{c:.4f}"


result=find_root(a,b,tolerans)            
print(result)