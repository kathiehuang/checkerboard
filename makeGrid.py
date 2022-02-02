import matplotlib.pyplot as plt
import numpy as np

practiceInput = np.array([[1,0,1,0,1,0],
                          [0,0,1,0,0,0],
                          [1,1,0,0,1,0],
                          [1,1,1,1,1,1],
                          [1,0,0,0,0,1],
                          [1,0,0,1,1,1]])

# takes in 6x6 numpy array, returns array for now 

def makeGrid(arr):
    plt.figure(figsize=(12,12))
    plt.imshow(arr.squeeze(), cmap = 'gray')
    plt.axis(False)
    plt.show()
    return arr

#add black border 
practiceInput = np.insert(practiceInput, 0, [0,0,0,0,0,0], axis = 0)
practiceInput = np.insert(practiceInput, len(practiceInput), [0,0,0,0,0,0], axis = 0)
practiceInput = np.insert(practiceInput, 0, 0, axis = 1)
practiceInput = np.insert(practiceInput, len(practiceInput[0]), 0, axis = 1)

#add white border 
practiceInput = np.insert(practiceInput, 0, [1,1,1,1,1,1,1,1], axis = 0)
practiceInput = np.insert(practiceInput, len(practiceInput), [1,1,1,1,1,1,1,1], axis = 0)
practiceInput = np.insert(practiceInput, 0, 1, axis = 1)
practiceInput = np.insert(practiceInput, len(practiceInput[0]), 1, axis = 1)
print(practiceInput)
makeGrid(practiceInput)

