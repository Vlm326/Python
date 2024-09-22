from tqdm import *
from time import *


s = "Hello, World!" * 1000000  # Example large string
def f(s):
    counter = {}
    for i in tqdm(range(len(s)), desc = 'Counting', ncols = 100, colour = 'green'):
        if i in counter.keys():
            counter[i] += 1
        else:
            counter[i] = 1

f(s)
    
