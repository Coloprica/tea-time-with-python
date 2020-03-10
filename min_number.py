def minimun(a, b):
	if a < b: 
		return a
	else:
		return b	

numbers = [-8, 20, -300, -1, -5, 1]

min = numbers[0]

for elem in numbers:
	min = minimun(min, elem)

def findSmallestInt(arr):
    smallest = arr[0]
    for item in arr:
        if item < smallest:
            smallest = item
    return smallest

print(findSmallestInt(numbers))