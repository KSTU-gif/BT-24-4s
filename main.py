import random

def roll_two_dice():
    """Функция возвращает сумму двух шестигранных кубиков"""
    return random.randint(1, 6) + random.randint(1, 6)

N = 1000  
results = {}   

for i in range(2, 13):
    results[i] = 0

for i in range(N):
    s = roll_two_dice()
    results[s] += 1

theory_counts = {
    2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6,
    8: 5, 9: 4, 10: 3, 11: 2, 12: 1
}

total_combinations = 36

print(f"{'Исход':<8} {'Процент симуляции':<20} {'Ожидаемый процент':<20}")
print("-" * 50)

for value in range(2, 13):
    percent_sim = results[value] / N * 100
    percent_expected = theory_counts[value] / total_combinations * 100
    print(f"{value:<8} {percent_sim:<20.2f} {percent_expected:<20.2f}")
