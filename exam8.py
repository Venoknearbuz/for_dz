#1
n = int(input())

max1 = 0
max2 = 0

for _ in range(n):
    num = int(input())

    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print("Наибольшее число:", max1)
print("Второе по величине число:", max2)

#2
input_string = input("Введите цены через пробел: ")
original_list = [int(x) for x in input_string.split()]

ascending_list = sorted(original_list)
descending_list = sorted(original_list, reverse=True)
reversed_list = original_list[::-1]

print("По возрастанию:", ascending_list)
print("По убыванию:", descending_list)
print("В исходном порядке:", original_list)
print("В обратном порядке:", reversed_list)

#3
class Necromancer:
    def __init__(self, mana):
        self.mana = mana

    def raise_skeleton(self):
        if self.mana >= 20:
            self.mana -= 20
            print(f"Скелет успешно призван! Осталось маны: {self.mana}")
        else:
            print("Недостаточно маны")


hero = Necromancer(50)
hero.raise_skeleton()
hero.raise_skeleton()
hero.raise_skeleton()
