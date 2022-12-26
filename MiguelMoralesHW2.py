"""
Made by Miguel Ernesto Morales Molina
matrikel-NR 15590763

"""


import matplotlib.pyplot as plt #import to use charts to show the data
import time # import for time functions

""" Function to read the data from the file"""
def readData():
    f = open("data.txt", "r") # read the file data
    data = f.read().split("\n") # we split every value in the string data and assig it to the list
    data.pop(len(data)-1) # remove the last value that is a blank space
    aux = [] #create a list to storage the data
    
    for value in data: #loop to add every line in the file to our list
        aux.append(float(value)) # we convert the data type to Float
    return aux

"""Funtion to draw the data"""
def draw(data):
    plt.plot(data) # here we create our chart for the data
    plt.show() # and show it


""" Funtion to do the bubble sort method"""
def bubbleSort(data,n):
    arr = data
   
    for j in range(0,n): # here we move for every item in our list
        for i in range(0,n-1): # and here we move from the beginning to the last not sort item
            if arr[i] > arr[i+1]: # compare the items
                arr[i],arr[i+1] = arr[i+1],arr[i] #swap items
        n-=1


    return arr

"""Function to do the selection sort method"""
def selectionSort(data):
    arr = data 
    n = len(arr) #initialize the value of n
    
    for currentItem in range(0,n-1): # for loop to move in the list

        currentMinimum = currentItem # we initialize our current minimun with our current item

        for j in range(currentItem+1,n):
            if(arr[j]<arr[currentMinimum]): # if a item is lower that our current minimum that is our new current minimum
                currentMinimum = j

        if(currentMinimum!=currentItem): #if our current minimum is different to our current item we swap
            arr[currentItem],arr[currentMinimum] = arr[currentMinimum],arr[currentItem]
    
    return arr

""" Function to make our timer"""
def timer(start,end):
    
    elapsedTime = end - start # we obtain our time used to run the code
    
    return elapsedTime


data = readData() # read the data
draw(data) # draw the data without sort

start = time.time() # start the timer
dataSort = bubbleSort(data,len(data)) # sort the data with the bubble sort method
end = time.time() # stop the timer
time1 = timer(start,end) # compute the time took to sort 
print("The bubble sort algorithm took ",time1," seconds") #print the result

data = readData() #read the data
start = time.time() # Start the timer 
dataSort = selectionSort(data) # sort the data with the selection sort method 
end = time.time() # end the timer 
time2 = timer(start,end) # compurte the time took to sort 
print("The selection sort algorithm took ",time2," seconds") #print the result 

if time1 < time2: 
    print("Bubble Sort is a", (time1-time2)/time2*100*-1, "% Faster than Selection Sort.")
else:
    print("Selection Sort is a", (time2-time1)/time1*100*-1, "% Faster than Bubble Sort.")
draw(dataSort) # draw the now the data sort
