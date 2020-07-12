#!/usr/bin/env python3

def simulateDiceRoll(NumRolls):
    '''
    simulate and get probability of dive rolls

    '''
    import random
    results=[0]*6
    for _ in range(NumRolls):
        roll = random.randint(1,6 )
        results[roll-1]+=1
    return results    

def unifromRolls():
    import numpy as np
    print('Enter NumTrails')
    NumTrails = int(input())
    print('Enter NumRolls')
    NumRolls= int(input())
    #results =[]
    #for _ in range(NumTrails):
    #   results.append(simulateDiceRoll(NumRolls=NumRolls))
   ## print(results)
    #res= [sum(i) for i in zip(*results)] 
    #for i,val in enumerate(res):
    #    print(f'Proportion of {i+1} :  {val/sum(res) :.6f}')

    ##With numpy
    results= np.zeros(shape=(1,6),dtype='int') 

    for _ in range(NumTrails):
        results=np.vstack((results,simulateDiceRoll(NumRolls=NumRolls))) 
   # res= [sum(i) for i in zip(*results)]
    #remove top placeholder row
    results=np.delete(results, (0), axis=0)
#    print(results)
   # print(resultsimes [:,5])
    print('Atleast one event for all faces of the dice')
    print(np.count_nonzero(results, axis=0))
    res =np.sum(results,axis=0)
   # print(res)
    print('###########Totals#######')
    for i,val in enumerate(res):
        print(f'Proportion of {i+1} :  {val/sum(res):.6f}')

             
if __name__ == "__main__":
    unifromRolls()
