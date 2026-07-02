#1
rating = int(input("Введите рейтинг от 1 до 10: "))
match rating:
    case 1 | 2 | 3:
        description = "Плохо"
        emoji = "❌"
        recommendation = "Требуются кардинальные изменения и исправление ошибок."
    case 4 | 5:
        description = "Удовлетворительно"
        emoji = "⚠️"
        recommendation = "Базовые элементы выполнены, но нужно поработать над качеством."
    case 6 | 7 | 8:
        description = "Хорошо"
        emoji = "👍"
        recommendation = "Отличный результат! Обратите внимание на мелкие детали для идеала."
    case 9 | 10:
        description = "Великолепно"
        emoji = "🔥"
        recommendation = "Потрясающая работа! Ничего менять не нужно, держите планку."
    case _:
        description = "Ошибка"
        emoji = "🚫"
        recommendation = "Пожалуйста, введите корректное число строго от 1 до 10."
print(f"Оценка: {description} {emoji}")
print(f"Рекомендация: {recommendation}")

#2
numbers = [10, 20, 30, 40]
numbers[1] = 17
numbers.extend([4, 5, 6])
numbers.pop(0)
numbers = numbers * 2
numbers.insert(3, 25)
print(numbers)

#3
import math

def solve(a, b, c):
    D = b ** 2 - 4 * a * c

    if D < 0:
        return []
    elif D == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return sorted([x1, x2])

print(solve(1, -3, 2))  
print(solve(1, -2, 1)) 
print(solve(1, 2, 5))  
