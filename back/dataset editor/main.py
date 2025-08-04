import os

import func


f = open("m.txt" , "r")
data = f.readlines()
r =  open("maine.txt" , "a+")

for i in data:
    r.write(func.high_reg_to_low(func.del_double_or_more_spaces(func.delete_symbols(i , ".,[]1234567890-!@#$%^&*()"))) + "\n")
    
r.close()