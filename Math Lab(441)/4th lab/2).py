import numpy as np
import scipy as linalg
def solve(A,B,X):
    a=linalg.inverse(A)@B
    print(a)
