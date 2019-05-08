# Uses python3

def fibNonRecursive(n):
    counter = 1
    array=[0,1]
    while counter < n:
        number = array[counter]+array[counter-1]   
#        print(number)
        counter = counter+1
        array.append(number)
    return array[-1]



def main():
    c = {0:0,1:1,2:1}
    n = int(input())
   
    
    print(fibNonRecursive(n,c))
    

if __name__ == "__main__":
    main()
    




