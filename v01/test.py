from collections import Counter
import numpy as np
import os

from wrd import wrd

weigh01 = np.load("weigh0_1.npy")
weigh12 = np.load("weigh1_2.npy")
ind = 1
while True :
    ind = int(input())
    