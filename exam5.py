#1
x1, y1, x2, y2 = map(int, input().split())

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')

#2
numbers = [10, 20, 30, 40, 50, 30]
target = int(input("Введите число: "))
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Индекс числа: {i}")
        found = True
        break  

if not found:
    print("Нет такого числа")

#3
def is_password_good(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit

print(is_password_good("Password123"))
print(is_password_good("12345678"))
print(is_password_good("qwerty"))
