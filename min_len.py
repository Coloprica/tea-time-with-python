def find_most_shortest_word(string):
	#print('Введите, пожалуйста, предложение:')
	#string = input()
	 
	words = string.split()
	 
	shortest = words[0]
	 
	for word in words[1:]:
	    if len(word) < len(shortest):
	        shortest = word 

	print(shortest)
	print(len(shortest))

find_most_shortest_word('валя препод')