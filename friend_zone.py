def show_friends(array):
	friends = [] 
	for item in array:
		if len(item) == 4:
			friends.append(item)
	if friends == []:
		answer = 'Друзей нет'
	else:
		answer = friends
	return answer

array = ["Rayan", "Yous", "Josef", "Mark"]
not_a_friends = ['ebobo', 'trololo']

print(show_friends(array))
print(show_friends(not_a_friends))
