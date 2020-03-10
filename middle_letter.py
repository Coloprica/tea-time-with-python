def middle_letter(string):
	length = len(string)
	middle_index = int(length/2)
	if length % 2 == 0:
		print(string[middle_index - 1] + string[middle_index])
	else:
		print(string[middle_index])
middle_letter('zdarovaaaa')
middle_letter('12345')

	




