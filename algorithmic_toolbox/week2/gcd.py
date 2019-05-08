#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:33:09 2019

@author: vladimiruspenskiy
"""

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
      return gcd(y,r)



def main():

    a,b = map(int, input().split())
   
    
    print(gcd(a,b))
    

if __name__ == "__main__":
    main()

