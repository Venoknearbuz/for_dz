#1
import random

secret_number = random.randint(1, 10)
print("Я загадал число от 1 до 10. У вас есть 3 попытки, чтобы угадать его!")

for attempt in range(1, 4):
    guess = int(input(f"Попытка {attempt}. Введите ваше число: "))

    if guess == secret_number:
        print("Поздравляю! Вы угадали число!")
        break
    elif guess < secret_number:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
else:
    print(f"К сожалению, попытки закончились. Я загадал число {secret_number}.")

#2
numbers = [10, 5, 23, 42, 8, 17, 91]

print("Длина списка:", len(numbers))
print("Последний элемент:", numbers[-1])
print("В обратном порядке:", numbers[::-1])
print("Содержит 5:", 5 in numbers)
print("Содержит 17:", 17 in numbers)
print("Без первого и последнего элементов:", numbers[1:-1])

#3
class Werewolf:
    def __init__(self, is_human=True):
        self.is_human = is_human

    def transform(self):
        self.is_human = not self.is_human

        if self.is_human:
            print("Персонаж превратился в человека!")
        else:
            print("Персонаж превратился в волка!")


monster = Werewolf()
monster.transform()
monster.transform()
monster.transform()
