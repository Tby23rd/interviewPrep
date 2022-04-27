import array

arr = array.array('i', [1, 2, 3, 1, 5])

print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")

print(".\r")

arr.append(4)
print("The popped element is : ", end="")
print(arr.pop(2))

# using remove() to remove 1st occurrence of 1
print(arr.remove(1))

# printing array after removing
print("The array after removing is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")

print("The new appended array is : ", end=" ")
for i in range(0, 4):
    print(arr[i], end=" ")

arr.insert(2, 5)

print(".\r")

print("The new array inserted is : ", end=" ")
for i in range(0, 5):
    print(arr[i], end=" ")

# Using index() to print index of 1st occurrence of 2
print("The index of 1st occurrence of 2 is : ", end="")

# Using reverse to reverse the array
arr.reverse()

# printing array after reversing
print("The array after reversing is : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")
