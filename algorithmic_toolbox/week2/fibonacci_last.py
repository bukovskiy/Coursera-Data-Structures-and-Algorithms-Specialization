# Uses python3

def fibLast(n):
    counter = 1
    array=[0,1]
    while counter < n:
        number = array[counter]%10+array[counter-1]%10   
#        print(number%10)
        counter = counter+1
        array.append(number%10)
    return array[-1]



    
def main():

    n = int(input())
    print(fibLast(n))
    
if __name__ == "__main__":
    main()
    


    




