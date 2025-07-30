import numpy as np 
import os
from addon import get_sentence_by_file , make_word_list
from config import hidden_layer , alfa , itr

sentences = get_sentence_by_file("realistic_english_sentences_5000.txt") #about len = ( min = 4  max =8 ) 
words = make_word_list(sentences=sentences)

one_matrix =  np.eye(hidden_layer)

def learning():
    min = 6 
    max = 0
    for i in itr: 
        for snt in sentences : #example of snt = ['they', 'attend', 'meetings', 'every', 'monday'] 
            

learning()