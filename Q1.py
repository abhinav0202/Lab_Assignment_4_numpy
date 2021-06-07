##1. Using numpy, WAP that takes an input from the user in the form of a list and calculate the
##frequency of occurrence of each character/integer in that list (count the number of
##characters).


import numpy as np

lst = np.array(list(input())) 

(unique, counts) = np.unique(lst, return_counts=True)
frequencies = np.asarray((unique, counts)).T

print(frequencies)



