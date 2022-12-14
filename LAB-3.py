'''Lab-3: Implement Quick Sort algorithm with all the necessary functions.'''

def partition(arr,low,high):
    '''A partition function to perform the partition process in the 
    passed array or a list'''
    # choosing the first element as the pivot in a list.
    pivotpoint = arr[low]  
    i , j = low + 1 , high  
    
    # compare each element with pivot
    while i <= j : 
        if arr[j] < pivotpoint and arr[i] > pivotpoint  : 
            arr[j],arr[i] = arr[i],arr[j]   # swap 
            
        if not arr[i] > pivotpoint : 
            i += 1
        
        if not arr[j] < pivotpoint:
            j -= 1
    
    arr[low],arr[j] = arr[j],arr[low] #swapping the pivot element with j
    
    return j  # returning the index of pivot element after setting it

def quickSort(array,low,high):
    '''A quick sort function to perform quicksort in the 
    passed array or a list'''
    
    if low < high:  
        # Find the pivot element such that
        # element smaller than pivot are on the left
        # and the element greater than pivot are on the right
        partition_index = partition(array,low,high) # fetches the index of pivot element
        
        # Recursive call to sort the left subarray of the pivot.
        quickSort(array,low,partition_index-1) 
        # Recursive call to sort the Right subarray of the pivot. 
        quickSort(array,partition_index+1,high) 
    

# Driver code

array=[96,77,69,96,11,22,6,55,45]
quickSort(array,0,len(array)-1)
print(array)
