#One dimensional array
#two dimensional array
#three dimensional array

import numpy as np

twoDArray = np.array([[11, 15, 10, 6], 
                      [10, 14, 11, 5], 
                      [12, 17, 12, 8], 
                      [15, 18, 14, 9]])

# newTwoDArray = np.insert(twoDArray, 4, [[1,2,3,4]], axis=0)
# print(newTwoDArray)

# newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=1)
# print(newTwoDArray)

def accessElement(array, rowIndex, columnIndex):
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        return "Incorrect index"
    return array[rowIndex][columnIndex]

def traverseTDArray(arr):
    for row in arr:
        for element in row:
            print(element)

def searchTDArray(arr, target):
    if len(arr) == 0:
        return "Array is empty"
    for row in range(len(arr)):
        for element in range(len(arr[0])):
            if arr[row][element] == target:
                return "Element found in the array"
            
# print(searchTDArray(twoDArray, 9))

def findPairs(arr, target):
    if len(arr) == 0:
        return
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            sum = arr[i] + arr[j]
            if arr[i] == arr[j]:
                continue
            elif sum == target:
                print([i,j])

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def maxProduct(arr):
    maxProduct = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i]*arr[j]
            if product > maxProduct:
                maxProduct = product
                pairs = str(arr[i]) + " ," +  str(arr[j])
    return [pairs, maxProduct]

# print(maxProduct(arr))

twoDArray2 = np.array([[1,2,3],
                       [4,5,6],
                       [7,8,9]])
                        
def rotateMatrix(arr):
    n = len(arr)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # save top
            top = arr[first][i]
            # 
            
            # left -> top
            arr[first][i] = arr[last-i][first]
            
            # bottom -> left
            arr[last-i][first] = arr[last][last-i]
            
            # right -> bottom
            arr[last][last-i] = arr[i][last]
            
            # top -> right
            arr[i][last] = top
    return arr

# print(rotateMatrix(twoDArray2))