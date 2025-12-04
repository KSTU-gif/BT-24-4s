import math

def factorial(num):
	if num <= 0:rtr
		return 1
	return num * factorial(num - 1)

def solve(x, n, i = 1, term = 1):

	if i == n + 1:
		return 0

	return term + solve(x, n, i + 1, term * (x / math.sqrt(factorial(i) + i * i * i)))

print(solve(12, 2))