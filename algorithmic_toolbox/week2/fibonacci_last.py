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

def fibLast(n):
    counter = 1
    array=[0,1]
    while counter < n:
        number = array[counter]%10+array[counter-1]%10   
#        print(number%10)
        counter = counter+1
        array.append(number%10)
    return array[-1]



    
n = input()
   
for i in range
print(fibNonRecursive(n))
    


    




