# Uses python3

def fib(n,c):
    if n in c:
        return c[n]
    else :
        result = fib(n-1, c)+fib(n-2, c)
        c[n]=result

    return result



def main():
    c = {0:0,1:1,2:1}
    n = int(input())
   
    
    print(fib(n,c))
    

if __name__ == "__main__":
    main()
    




