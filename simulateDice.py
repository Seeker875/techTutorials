#!/usr/bin/env python3

def simulateDiceRoll(NumRolls):
    '''
    simulate and get probability of dive rolls

    '''
    import random
    results=[0]*6
    for _ in range(NumRolls+1):
        roll = random.randint(1,6 )
        results[roll-1]+=1
    return results    

def main():
    #import numpy as np
    print('Enter NumTrails')
    NumTrails = int(input())
    print('Enter NumRolls')
    NumRolls= int(input())
    results =[]
    for _ in range(NumTrails):
       results.append(simulateDiceRoll(NumRolls=NumRolls))
   # print(results)
    res= [sum(i) for i in zip(*results)] 
    for i,val in enumerate(res):
        print(f'Proportion of {i+1} :  {val/sum(res) :.6f}')
             
if __name__ == "__main__":
    main()
