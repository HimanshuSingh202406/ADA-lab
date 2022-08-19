# Function
def binary_search(arr, a, low, high):

    # while loop check is low is less then high
    while low <= high:

        mid = low + (high - low)//2

        if arr[mid] == a:
            return mid

        elif array[mid] < a:
            low = mid + 1

        else:
            high = mid - 1

    return -1

ar = [12,24,36,48,60,72,84]
a = 48

print("The given array is", ar)


print("Element to be found is ", a)

index = binary_search(ar, a, 0, len(ar)-1)

if index != -1:
    print("The Index of the element is " + str(index))
else:
    print("Element Not found")
