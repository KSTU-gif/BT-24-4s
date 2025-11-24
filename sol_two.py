def sum_unique_digits(num, current = 0, repeat = 0):
	if (num <= 0):
		return 0
	
	if repeat == current:
		return sum_unique_digits(num // 10, num % 10, repeat)
	
	current_num = num % 10
	return current + sum_unique_digits(num // 10, current_num, current_num)	


print(sum_unique_digits(112233))