def sum(x, i, n):
	if i == 1:
		return 1
	return sum(x*i/(i*2 + 1))
print(sum(2, 3, 3))
