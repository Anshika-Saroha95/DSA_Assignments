# Do not use another list/array, set, dict, sorting, or built-in shortcuts that defeat the purpose of the exercise.
# Find the Maximum Element Given an integer array, find the largest element without using max().
# arr = [12, 45, 7, 89, 34, 67]
#  # Output: 89 

arr = [12, 45, 7, 89, 34, 67]
max_element = arr[0]
for i in range(1, len(arr)):
    if arr[i]>max_element:
        max_element = arr[i]
print(max_element)



# Find the Minimum Element Find the smallest element without using min().
# arr = [12, 45, 7, 89, 34, 67] 
# Output: 7 

arr = [12, 45, 7, 89, 34, 67] 
min_element = arr[0]
for i in range(1, len(arr)):
    if arr[i] < min_element:
        min_element = arr[i]
print(min_element)  


# Find Maximum and Minimum Together Find both in a single traversal. 
# arr = [20, 5, 40, 10, 80, 15] 
# Maximum: 80 # Minimum: 5 

arr = [20, 5, 40, 10, 80, 15]
max_element = arr[0]
min_element = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]
    if   arr[i] < min_element:
        min_element = arr[i]
print("Max element : ",max_element)
print("Min element : ",min_element)


# Calculate Sum of Array Find the sum without using sum().
# arr = [10, 20, 30, 40] 
# # Output: 100 

arr = [10, 20, 30, 40]
sum = 0
for i in range(0,len(arr)):
    sum = sum + arr[i]
print(sum)


# Calculate Average Calculate the average without using sum(). 
# arr = [10, 20, 30, 40, 50]
 # Output: 30

arr = [10, 20, 30, 40, 50]
total = 0
for i in range(0 ,len(arr)):
    total = total + arr[i]
    Average = total/len(arr)
print(Average)


# Count Even Numbers Count how many elements are even. 
# arr = [10, 15, 22, 33, 40, 51]
 # Output: 3 

arr = [10, 15, 22, 33, 40, 51]
count = 0
for i in range(0, len(arr)):
    if arr[i] % 2 == 0:
        count += 1
print(count)


# Count Positive, Negative and Zero Values
# arr = [-5, 10, 0, -3, 8, 0, 7]
#  # Positive: 3 
# Negative: 2 # Zero: 2 

arr = [-5, 10, 0, -3, 8, 0, 7]
positive = 0
negative = 0
zero = 0
for i in range(0, len(arr)):
    if arr[i] > 0:
        positive +=1
    elif arr[i] < 0:
        negative +=1
    else :
        zero +=1
print("Positive :",positive)
print("Negative :",negative)
print("Zero : ",zero)



# Linear Search Find the index of a target value. Return -1 if it doesn't exist.
# arr = [10, 30, 50, 70, 90] 
# target = 70 
# Output: 3 

arr = [10, 30, 50, 70, 90] 
target = 70
for i in range(0,len(arr)):
    if arr[i] == target:
        print(f"Found on index {i}")
        break
else:
    print(-1)


# Reverse an Array In-Place Reverse the original array without creating another array.
# arr = [10, 20, 30, 40, 50] 
# Output: [50, 40, 30, 20, 10] 

arr = [10, 20, 30, 40, 50] 

start = 0
end = len(arr) - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print(arr)



# Check Whether an Array Is Sorted Check whether the array is sorted in ascending order.
# arr = [10, 20, 30, 40, 50] 
# Output: True arr = [10, 30, 20, 40] # Output: False 

arr = [10, 20, 30, 40, 50]
arr = [10, 30, 20, 40]
sorted = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sorted = False
        break
print(sorted)


# Find the Second Largest Element Find the second largest distinct value without sorting.
# arr = [10, 40, 20, 50, 30]
 # Output: 40 

arr = [10, 40, 20, 50, 30]
largest = arr[0]
secondLargest = arr[0]

for i in range(0, len(arr)):
    if arr[i] > largest:
        secondLargest = largest
        largest = arr[i]
    elif arr[i] > secondLargest and arr[i] != largest:
        secondLargest = arr[i]

print(secondLargest)


# Find the Second Smallest Element Find the second smallest distinct value without sorting.
# arr = [20, 5, 10, 40, 15]
 # Output: 10 

arr = [20, 5, 10, 40, 15]
smallest = arr[0]
second_smallest = arr[0]
for i in range(0, len(arr)):
    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]
    elif arr[i] < second_smallest and arr[i] != smallest:
        second_smallest = arr[i]

print(second_smallest)


# Move All Zeros to the End In-Place Keep the relative order of non-zero elements.
# arr = [0, 1, 0, 3, 12]
 # Output: [1, 3, 12, 0, 0] 

arr = [0, 1, 0, 3, 12]
start = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[start], arr[i] = arr[i], arr[start]
        start += 1
print(arr)

# Move All Negative Numbers to the Beginning In-Place Rearrange the array so negative numbers appear before non-negative numbers. The relative order does not need to be preserved.
# arr = [10, -2, 5, -7, 8, -1]
 # One valid result: # [-1, -2, -7, 5, 8, 10] 

arr = [10, -2, 5, -7, 8, -1]
start = 0
for i in range(len(arr)):
    if arr[i] < 0:
        arr[start], arr[i] = arr[i], arr[start]
        start +=1
print(arr)        

# Remove Duplicates from a Sorted Array In-Place Return the number of unique elements and place those unique elements at the beginning.
# arr = [1, 1, 2, 2, 3, 3, 4]
 # First part of array: # [1, 2, 3, 4, ...] # Output: # 4 
 

arr = [1, 1, 2, 2, 3, 3, 4]

unique = 1
for i in range(1, len(arr)):
    if arr[i] != arr[unique - 1]:
        arr[unique] = arr[i]
        unique += 1

# print(arr[:unique])
print(unique)