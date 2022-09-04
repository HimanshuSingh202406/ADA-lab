def mergeSort(arr):
    if len(arr) > 1:

        r = len(arr)//2
        leftArray = arr[:r]
        rightArray = arr[r:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1

def display(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [11, 7, 9, 13, 6, 0, 22, 2, 64, 69, 96]
    
    print("Original array:->")
    display(arr)
    
    mergeSort(arr)

    print("Sorted array:->")
    display(arr)
