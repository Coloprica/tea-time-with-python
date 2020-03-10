def crop_word(string):
	return string[1:-1]

cropped_word = crop_word('strrokaaa')
cropped_word = crop_word('')
print('Получилось : ' , cropped_word)

a = 'python'
b = 'is awesome'
answer = a[0] + b[-1] + a[-1] + b[:2]
print(answer) 