# python3


def maxPairwise(array):
    
    a = max(array)
    array.remove(a)
    b = max(array)
    return a*b

if __name__ == '__main__':
    input_n = int(input())
    array = [int(i) for i in input().split()]

    print(maxPairwise(array))
    
