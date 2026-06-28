#1
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if abs(x1 - x2) == abs(y1 - y2):
    print("YES")
else:
    print("NO")

#2
word = input("Введите слово: ")
original_list = list(word)
reversed_list = original_list[::-1]

if original_list == reversed_list:
    print("Это палиндром")
else:
    print("Не палиндром")
#3
class Survivor:
    def __init__(self, name: str):
        self.name = name
        self.inventory = []

    def add_loot(self, item: str):
        self.inventory.append(item)
        print(f"Текущий инвентарь {self.name}: {self.inventory}")


survivor = Survivor("Алекс")
survivor.add_loot("Аптечка")  
survivor.add_loot("Фонарик")  
survivor.add_loot("Нож")
