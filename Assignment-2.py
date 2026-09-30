# Solve these questions by using def and return 

# Question 1:
# Find the largest element in an array without using the max() function.
arr = [43,67,25,68,35,78,35,57,46]
def largest(arr):
    largest_element  = arr[0]

    for i in arr:
        if i>largest_element:
            max_element = i

            return largest_element
print (largest(arr))


# Question 2:
# Find the second largest element in an array without using sorting or max().
arr = [43,67,25,68,35,78,35,57,46]
def second_largest(arr):
    second_largest = arr[0]
    largest = arr[0]

    for i in range(1,len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    return second_largest
print(second_largest(arr))


# Question 3:
# Reverse an array without using slicing.
def reverse(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1
    return arr
arr = [43,67,25,68,35,78,35,57,46]
print(reverse(arr))

# Question 4:
# Check whether an array is sorted in ascending or descending order.
# Return True if sorted, otherwise return False.
def check_sorted(arr):
    if arr[0] > arr[1]:
        for i in range(0,len(arr)-1):
            if arr[i] < arr[i+1]:
                return False
    else:
        for i in range(0,len(arr)-1):
            if arr[i] > arr[i+1]:
                 return False
    return True
# arr = [50,40,30,20,10]
arr = [10,20,30,40,50]
print(check_sorted(arr))

# Question 5:
# Remove duplicates from a sorted array in-place.
# Return the number of unique elements.
arr = [20,20,30,40,40,50]
def remove_duplicates(arr):
    unique_elements = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_elements - 1]:
            arr[unique_elements] = arr[i]
            unique_elements +=1
    return unique_elements
# print("Num of unique element : " ,remove_duplicates(arr)) 
# print(arr[:remove_duplicates(arr)])
# print(arr[:4])

k = remove_duplicates(arr)

print("Number of unique elements:", k)
print("Unique elements:", arr[:k])



# Question 6:
# Rotate an array to the right by K positions.
# Use the def function and return the rotated array.

          