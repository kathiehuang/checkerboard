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

    #add black border 
    arr = np.insert(arr, 0, [0,0,0,0,0,0], axis = 0)
    arr = np.insert(arr, len(arr), [0,0,0,0,0,0], axis = 0)
    arr = np.insert(arr, 0, 0, axis = 1)
    arr = np.insert(arr, len(arr[0]), 0, axis = 1)

    #add white border 
    arr = np.insert(arr, 0, [1,1,1,1,1,1,1,1], axis = 0)
    arr = np.insert(arr, len(arr), [1,1,1,1,1,1,1,1], axis = 0)
    arr = np.insert(arr, 0, 1, axis = 1)
    arr = np.insert(arr, len(arr[0]), 1, axis = 1)
    plt.figure(figsize=(5,5))
    plt.imshow(arr.squeeze(), cmap = 'gray')
    plt.axis(False)
    plt.savefig('apriltag.png', dpi=300, bbox_inches='tight', pad_inches = 0)
    plt.show()
    return 'apriltag.png'



#print(practiceInput)
makeGrid(practiceInput)

