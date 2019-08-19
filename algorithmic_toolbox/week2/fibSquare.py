# Uses python3

def pisano(m):
    if m == 1:
        return 1
    if m == 2:
        return 3
    a,b, = 0, 1
    c=a+b 
    for i in range(m**2): 
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            return i + 1;
        
def fibNonRecursive(n):
    if n == 0:
        return 0
    counter = 1
    array=[0,1]
    while counter < n:
        number = array[counter]+array[counter-1]   
#        print(number)
        counter = counter+1
        array.append(number)
    return array[-1]
    
def largeFibonacci(n):
    
     
    pis = pisano(10)   
#    print(pis)
    num = fibNonRecursive(n%pis)   
#    print(num)
    return num%10



def main():
    n = int(input())
    print((largeFibonacci(n)*largeFibonacci(n+1))%10)
    

if __name__ == "__main__":
    main()
    




