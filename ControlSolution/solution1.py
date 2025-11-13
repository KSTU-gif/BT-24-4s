# Вариант 5

def solve(k = 1, n):
	if k >= n:
		return 0
	else:
		exp = (2 * k + 1) * (2 * k + 1)
		return 1/exp + solve(k + 1; n)

n = int(input("Введите n:"))

result = solve(k, n)

print(f"Результат: {result}")