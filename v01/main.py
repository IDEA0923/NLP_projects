from collections import Counter
import numpy as np
import os

from wrd import wrd
from funcactivation import relu , relu_re , softmax, softmax_backward
f = open("realistic_english_sentences_5000.txt" , "r")
sent = f.readlines()
sentence = []
word2ind = list()
min_len = 6
max_len = 0
for l in sent:
    
    buff = ""
    a = list()
    for i in l :
        if i == ' ' or i == '\n':
            a.append(buff)

            if buff not in word2ind:
                word2ind.append(buff)
                print("NEW WORD:" + buff)
            buff = ""
        else:
            buff = buff + i
    print(a)
    if(len(a) > max_len):
        max_len = len(a)
    if(len(a) < max_len):
        min_len = len(a)
    
    sentence.append(a)
#print(word2ind.__sizeof__())
print(len(sentence[1]))
print(len(sentence))
print(f"\nmin len = {min_len}\t max_len =  {max_len}\n")
print(len(wrd))

# - - - -> +

print(f"w2i =  {len(word2ind)}")
# inp = np.zeros(len(word2ind))
# weigh1_2 = 
# for in1 in range(2):
#     for i in 
wrd
hidden_layer  , alfa , itr , top = 100 , 0.0001 , 6 , 10
layer0 = np.zeros(len(wrd))
weigh0_1 = np.random.rand(len(wrd) ,hidden_layer )
weigh1_2 = np.random.rand(hidden_layer  , len(wrd))


#layer1 = np.zeros(hidden_layer)
#layer2  = layer1.dot(weigh1_2)
for i1 in range(itr):
    for i2 in range(len(sentence)): 
        layer0 = np.zeros(len(wrd)) 
        inp =  sentence[i2]

        for i in range(3):
            if inp[i] in wrd :
                layer0[wrd.index(inp[i])] = 1
        #print(f"layer0 {str(layer0)}")
        layer1 = layer0.dot(weigh0_1)

        #print(f"layer 1 = {layer1}")
        
        layer2  = layer1.dot(weigh1_2)
        
        layer3 =layer2
         
        if not(i2 % 10) :
            print(f"TOP {top}: ")
            arr = np.array(layer3)
            print(type(layer3), layer3)
            # top_of_val = np.argsort(arr)[-top][::-1]
            top_of_val = np.argsort(arr)[-top:][::-1]
            ind = 1
            snt = list()
            for i in range(3):
                snt.append(inp[i])
            print(snt)
            print(f"True = {inp[3] }")
            for i in top_of_val:
                ind = ind + 1 
                print(f"\t{i} . {wrd[i]}  == {arr[i]}")
        
        #########################################

        tr = inp[3] 
        target = np.zeros(len(wrd))
        target[wrd.index(tr)] = 1


        diff_l3 = (layer3 - target )
        
         
        diff_l1 = diff_l3.dot(weigh1_2.T)
        # #print((diff_l3 * alfa  * layer1 ).shape)
        # weigh0_1 = weigh0_1 - (diff_l1 * alfa * layer0)
        # weigh1_2 = weigh1_2 - (diff_l3 * alfa  * layer1 )
        weigh1_2 -= alfa * np.outer(layer1, diff_l3)  # [100, len(wrd)]
        weigh0_1 -= alfa * np.outer(layer0, diff_l1)  # [len(wrd), 100]


np.save("weigh0_1.npy" , weigh0_1)
np.save("weigh1_2.npy" , weigh1_2)
