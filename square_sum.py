def sum_of(array):
	sum = 0
	for item in array:
		sum = sum + item**2
	
	print(sum)

sum_of([1, 3, 4, 5])