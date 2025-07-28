import numpy as np 
from funcactivation import relu
#w =  np.random.rand(3,4)
w = [10 , -2, 12 , -0.6]

print(relu(w))


"""
for i1 in range(itr):
    for i2 in range(2): 
        layer0 = np.zeros(len(wrd)) 
        inp =  sentence[i2]

        for i in range(3):
            if inp[i] in wrd :
                layer0[wrd.index(inp[i])] = 1
        print(f"layer0 {str(layer0)}")
        layer1 = relu(layer0.dot(weigh0_1))

        print(f"layer 1 = {layer1}")
        
        layer2  = layer1.dot(weigh1_2)
        
        layer3 = softmax(layer2)
         
        if True :
            print("TOP : ")
            top_of_val = np.argsort(layer3)[-top][::-1]
            ind = 1
            for i in top_of_val:
                print(f"\t{ind} . {wrd[i]}  == {layer3[i]}")
"""