import numpy as np

def softmax(n):
    x = np.atleast_2d(n)
    temp = np.exp(x)
    return  temp / np.sum(temp , axis=1 , keepdims=True)

