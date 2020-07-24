'''
    Assignment 2
    Leslie N. Kodjoe
'''
import random
import time

def Binary_Search(array,target,high, low):
    
    if high >= low:
        #Divide array into two
        middle =(high + low)//2

        if  array[middle]== target:
            return middle
        
        #When search is smaller than middle element chosen
        elif array[middle]> target:
        #Function is called again recursively to search the left half
            return Binary_Search(array,target,middle-1,low)

        else:
        #Function is called again recursively to search the right half
            return Binary_Search(array,target,high,middle+1)
    else:
        return -1
    


def Interpolation_Search(array,target,N):#Size =N
    #Create two indexes
     high=(N-1)
     low=0

    #With sorted array in main, confirm if target is present between high and low
     while (low<=high and target>=array[low] and target<=array[high]):
         if high == low:
             if array[low]==target:
                 return low
             else:
                 return -1

         Pos = low +int((float(high-low)*(target-array[low]))//(array[high]-array[low]))

        #Checks if target is located
         if array[Pos] ==target:
             return Pos

        #Checks if target is in high portion
         if array[Pos]< target:
             low= Pos+1
             
        #checks if target is in low portion
         else:
             high= Pos-1

     return -1


def main(limit):
    array=[]
    #creates random numbers for array with a defined limit
    array=random.sample(range(1,32767),limit)

    #sorts the random array
    array.sort()
  
    N = len(array)
    target=random.randint(1,32767)
    print("Target is ",target)

    #Checks time when function begins to run
    startB=time.time()
    index_BSearch=Binary_Search(array,target,len(array)-1,0)
    endB=time.time()

    #Checks time when function begins to run
    startInter=time.time()
    index_InterSearch = Interpolation_Search(array,target,N)
    endInter=time.time()

    #Conditions to check if Element is found or not
    if index_BSearch!=-1:
        print("Element found with Binary Search is at index: ",index_BSearch)
    else:
        print("Element not found using Binary Search")
        print("The Runtime is %f msec" %(endB-startB))
        
    print()
    if index_InterSearch!=-1:
        print("Element found with Interpolation Search is at index: ",index_InterSearch)
    else:
        print("Element not found using Interpolation Search")
        print("The Runtime is %f msec" %(endInter-startInter))


#Runs main
main(100)
print()
main(1000)
print()
main(5000)




            
