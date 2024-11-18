import numpy as np

def save_array2CSV(a):
    np.savetxt("brain_sample.csv", a, delimiter=",", fmt="%.6f")
    
def readCSV(filepath = 'brain_average.csv'):
    data = np.genfromtxt(filepath, delimiter=",", dtype=float)
    return data