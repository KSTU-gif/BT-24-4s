# Вариант 5

def char_replace(counter = 0, str, old, new):
	str_length = len(counter)
	old_length = len(old)
	current = 0
	current_str = ""
	
	for i in range(counter, old_length):
		current = counter + i
		current_str = current_str + str[i]
	
	depth = 0
	if current_str == new:
		for i in range(counter, current):
				
			str[i] = new[depth]
			depth += 1

	return char_replace(counter + 1, str, old, new) 

s = input("Введите s:")
old = input("Введите old:")
new = input("Введите new:")

result = char_replace(0, s, old, new)

print(f"Result: {result}")
