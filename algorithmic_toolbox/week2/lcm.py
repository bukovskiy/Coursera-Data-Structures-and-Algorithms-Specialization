# Uses python3


def gcd(a, b):
  if a == 0 or b == 0:
      return 0
  if a >= b:
      x,y = a,b
  else:
      x,y = b,a
      
  r = x%y
  if r == 0:
      return y
  else:
      return int(gcd(y,r))

def main():
    n,m = map(int, input().split())


    print(int(int(n*m)//gcd(n,m)))

    


if __name__ == "__main__":
    main()
    
 

