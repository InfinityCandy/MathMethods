import numpy as np
import math
from _overlapped import NULL

"""Softmax function to solve NxN dimensional matrix"""
"""Python version: 3.5"""

#EXAMPLE MATRIX
uniMatrix = np.array([1, 2, 3, 6])
#multiMatrix = np.array([[1, 2, 3, 6], [2, 4, 5, 6], [3, 8, 7, 6]])

#Function softmax
def softmax(matrix):
    #Get number of rows to determinate if it's a uni-dimensional matrix
    rows = len(matrix)
    
    #Validates if the matrix is type of NxN, so if the first element is a np.array is a NxN matrix
    if type(matrix[0]) is np.ndarray:
        col = len(matrix[0])
      
    #If not then the number of columns in the matrix is 1  
    else:
        col = 1
        
    #Part of the function which is for uni-dimensional matrix  
    if col == 1:
        yi = []
        s = []
        
        #Get "e^i" elevated to each element of the matrix and append the results to an array
        for i in matrix:
            yi.append(math.exp(i))
            
        #As the number of columns is just one, all we need to do is add up each element of the matrix
        yj = sum(yi)
        
        #Then divide each element of the array "yi" between "yj" and append the result to the array "s"
        for i in yi:
            s.append(i/yj)
        
        #The function returns the result in the type of a numpy array
        return np.array(s)
    
    #Part of the function which is for NxN matrix
    else:
        yi = []
        yj = []
        
        #We iterate through each row in the matrix
        y = 0
        while y < rows:
            temp = []
            
            #We iterate through each column in the matrix
            w = 0
            while w < col:
                #Get an element in a specific position at "y" (row) and "w" (column) an elevate "e" to that pow and append the result to a temporal array, which corresponds to an a row
                temp.append(math.exp(matrix[y][w]))
                
                w = w + 1
            
            #Append each row to the matrix yi
            yi.append(temp)
            y = y + 1
    
    
        yj = []
        
        w = 0
        #We iterate through each column and row, so we can get every value of each column.
        while w < col:
            #We need to add up every value of each column and store it in this var and reset it ant the beginning of the cycle.
            add = 0
            
            y = 0
            #We iterate through each row
            while y < rows:
                #Add up the value of the position "w" (column) and "y" (row)
                add = add + yi[y][w] 
                y = y + 1
             
            #Append the value of every sum. 
            yj.append(add)  
            w = w + 1
         
         
        #The result will be a matrix, so we will store it in the array s  
        s = []
        y = 0
       # w = 0
       
       #Finally we divide the values of the matrix "yi" of each "w" (row) between the values of each element "w" (row) in yj.
        while y < rows:
            w = 0
            temp = []
            
            while w < col:
                temp.append(yi[y][w] / yj[w])
                
                w = w + 1
            
            #Each cycle returns a uni-dimensional temporal array, which corresponds to a row of the final matrix, so we append it to the array S (result).  
            s.append(temp)    
            y = y + 1
            
            
    return np.array(s)
    
    
print(softmax(uniMatrix))
    
    