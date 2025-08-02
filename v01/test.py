from collections import Counter
import numpy as np
import os
import random

from wrd import wrd # len = 153
top = 10
rng = 3
end_of_p = " "
weigh01 = np.load("weigh0_1.npy")
weigh12 = np.load("weigh1_2.npy")
ind = 1
words =  [wrd[92] , wrd [65] , wrd[35]]
while True :
    
    ind = int(input())
    
    for i in words:
        print(i , end=end_of_p)

    for d in range(ind):
        l0 = np.zeros(len(wrd))
        for i in range(3):      #initialization words 
            l0[wrd.index(words[i])] = 1
            #print(l0)
        l1 = l0.dot(weigh01)
        l2 = l1.dot(weigh12)
        w = ""
        if True :
            arr =  np.array(l2)
            top_of_val = np.argsort(arr)[-top:][::-1]
            rand = random.randint(0 , rng - 1)
            for i in top_of_val:
                ind = ind + 1 
                #print(f"\t{i} . {wrd[i]}  == {arr[i]}")
            w = wrd[top_of_val[rand]]
            #print(f"sentence = {words[0]}  {words[1]} {words[2]} {w}")
        print(w , end=end_of_p)
        if True : # remake words
            words[0] = words [1]
            words[1] = words [2]
            words [2] = w 
        
