import numpy as np

def calculate(input):
    """Calculate the mean, variance, std, max, min and sum of rows, columns and elements in a 3x3 matrix
        Input = list of 9 digits
    """
    operations = {'mean':'mean','var':'variance','std':'standard deviation','max':'max','min':'min','sum':'sum'}
    calculations = {}
    
    if len(input) == 9:
        array = np.array([input[0:3],input[3:6],input[6:9]])
        for operation,name in operations.items():
            func = getattr(np,operation)
            m1 = func(array,axis=1).tolist()
            m2 = func(array,axis=0).tolist()
            m = func(array).tolist()
            stats[name]= [m2,m1,m]
    else:
        print (ValueError("List must contain nine numbers"))

    return calculations
