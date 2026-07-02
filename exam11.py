#1
num_str = input("Введите натуральное число: ")
last_digit = num_str[-1]

count_3 = 0
count_last_digit = 0
count_even = 0
sum_greater_5 = 0
product_greater_7 = 1
has_greater_7 = False
count_0_and_5 = 0

for char in num_str:
    digit = int(char)

    if digit == 3:
        count_3 += 1

    if char == last_digit:
        count_last_digit += 1

    if digit % 2 == 0:
        count_even += 1

    if digit > 5:
        sum_greater_5 += digit

    if digit > 7:
        product_greater_7 *= digit
        has_greater_7 = True

    if digit == 0 or digit == 5:
        count_0_and_5 += 1

if not has_greater_7:
    product_greater_7 = 0

print("Количество цифр 3:", count_3)
print("Число повторений последней цифры:", count_last_digit)
print("Количество четных цифр:", count_even)
print("Сумма цифр больше 5:", sum_greater_5)
print("Произведение цифр больше 7:", product_greater_7)
print("Количество цифр 0 и 5:", count_0_and_5)

#2
line1 = "1 3 5 7"
line2 = "3 4 5 8 9"
line3 = "0 5 9 10"
all_possible_numbers = set(range(11))

set1 = set(int(x) for x in line1.split())
set2 = set(int(x) for x in line2.split())
set3 = set(int(x) for x in line3.split())

present_numbers = set1 | set2 | set3
missing_numbers = all_possible_numbers - present_numbers

print("Числа, которые отсутствуют во всех трех строках:", sorted(list(missing_numbers)))
