'''
Rounding up after dividing in Python

James Gaboardi, 2015


GNU LESSER GENERAL PUBLIC LICENSE
    Version 3, 29 June 2007
        Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
            Everyone is permitted to copy and distribute verbatim copies
                of this license document, but changing it is not allowed.
'''
    

# you only need numpy for creating random integers
import numpy as np

X = np.random.randint(0,5,10)
X = list(X)
print X, ' --> ', len(X)
New_List = []
for x in X:
    if x < 1:
        pass
    elif x == 1:
        New_List.append(x)
    else:
        New_List.append(int(x/2)+(x%2>0))
        
print New_List, ' --> ', len(New_List)  