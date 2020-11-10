import numpy as np 

def load_nonlinear_example1():
    x = np.array([[1,0.0],[1,2.0],[1,3.9],[1,4.0]])
    y = np.array([4.0,0.0,3.0,2.0])
    return x,y

def polynomial3_features(input):
    ploy2 = input[:,1:]**2
    ploy3 = input[:,1:]**3
    return np.c_[input,ploy2,ploy3]