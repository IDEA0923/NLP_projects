import numpy as np
import os
from addon import get_sentence_by_file , make_word_list
from my_func_math import softmax
from config import hidden_layer , alfa , itr

sentences = get_sentence_by_file("realistic_english_sentences_5000.txt") #about len = ( min = 4  max =8 )
words = make_word_list(sentences=sentences)

one_matrix =  np.eye(hidden_layer)
weigh1 = np.random.rand(len(words) , hidden_layer )# ( число нейронов, сколько каждый из них имеет весов от l0)
weigh2 = np.random.rand(hidden_layer , len(words) )

def learning():

    for i in range(itr):
        for snt in sentences : #example of snt = ['they', 'attend', 'meetings', 'every', 'monday']
            print(snt)
            l1 = np.zeros(hidden_layer)
            for i1 in range(len(snt) - 1):
                #print(i1)
                l1 = weigh1[words.index(snt[i1])] + l1.dot(one_matrix)
            print(len(l1))#100
            
            l2 = l1.dot(weigh2)
            print(softmax(l2))

learning()

# ['they', 'attend', 'meetings', 'every', 'monday']
# they
# attend
# meetings
# every