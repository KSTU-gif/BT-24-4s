#1 вариант
def recu(x, n):
	if n == 1:
		return privet(x, 1) / fact(1)
	return privet(x, n) / fact(n) + recu(x, n - 1)
print(recu)qfwqwf