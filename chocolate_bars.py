def break_chocolate(n,m):
	if type(n) == int and isinstance(m, int) and m > 0 and n > 0:
		result = m*n-1	
		return result
	else: 
		return 0

		
break_chocolate(1,1)
result = break_chocolate(-20,1)
print(result)

