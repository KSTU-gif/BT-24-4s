#1 вариант
def remove_digits(s, i=0):
	if i == len(s):
		return ""

	ch = "" if is_digit(s[i]) else s[i]
	return ch + remove_digits(s, i + 1)
print(remove_digits)