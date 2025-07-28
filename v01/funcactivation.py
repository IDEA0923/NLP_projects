import numpy as np
def relu(layer)-> list:
    l2 = list()
    for i in layer:
        one_or_zero =  int(i > 0)
        #print(one_or_zero)
        i = i * one_or_zero
        l2.append(i)
        #print(i)
    #print (l2)
    return l2

def relu_re(layer)->list:
    l2 = list()
    for i in layer:
        one_or_zero =  int(i > 0)
        l2.append(one_or_zero)
    #print (l2)
    return l2

def sigmoid(layer)->list:
    l2 = list()
    for i in layer:
        l2.append(1/(1 + np.exp(-i)))
    return l2

def sigmoid_re(layer)->list:
    l2 =  list()
    for i in layer:
        l2.append(i * (1 - i))
    return l2

def softmax(layer)->list:
    buff =  np.exp(layer)
    buff/=  np.sum(buff)
    return buff.tolist()

#fucked rand space of symbol , but i get this mindless def from book ...
# def softmax_re(layer)->list:
#     tmp = (layer - True)
#     layer =  tmp/len(True)


#from AI
def softmax_backward(softmax_output, grad_output):
    s = softmax_output.reshape(-1,1)
    jacobian = np.diagflat(s) - np.dot(s, s.T)
    return np.dot(jacobian, grad_output)