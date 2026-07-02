#1
start_count = int(input("Введите стартовое количество организмов: "))
daily_growth = float(input("Введите среднесуточное увеличение (%): "))
days = int(input("Введите количество дней: "))

current_population = start_count

for day in range(1, days + 1):
    current_population = current_population * (1 + daily_growth / 100)

    print(f"День {day}: {current_population:.2f}")

#2
items = [10, 50, 20, 100, 90, 30]
N = int(input("Сколько предметов можно взять? N = "))
sorted_items = sorted(items, reverse=True)
max_value = sum(sorted_items[:N])

print(f"Максимально возможная ценность предметов: {max_value}")

#3
def print_perm_time_call(msc_time):
    msc_hours, msc_minutes = map(int, msc_time.split(':'))
    perm_hours = (msc_hours + 2) % 24
    perm_minutes = msc_minutes

    print(f"Созвон будет в {perm_hours:02d}:{perm_minutes:02d}")

print_perm_time_call("15:30")
print_perm_time_call("23:15")
print_perm_time_call("08:05")
