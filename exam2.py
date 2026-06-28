#1
try:
    pocket = int(input("Введите номер кармана рулетки (от 0 до 36): "))

    if pocket < 0 or pocket > 36:
        print("ошибка ввода")

    elif pocket == 0:
        print("зеленый")
        
    elif (1 <= pocket <= 10) or (19 <= pocket <= 28):
        if pocket % 2 != 0:
            print("красный")
        else:
            print("черный")

    elif (11 <= pocket <= 18) or (29 <= pocket <= 36):
        if pocket % 2 != 0:
            print("черный")
        else:
            print("красный")

except ValueError:
    print("ошибка ввода")

#2
set1 = set(map(int, input("Введите первую строку ID: ").split()))
set2 = set(map(int, input("Введите вторую строку ID: ").split()))
set3 = set(map(int, input("Введите третью строку ID: ").split()))

full_range = set(range(11))
found_ips = set1 | set2 | set3
missing_ids = list(full_range - found_ips)
missing_ids.sort()
print(missing_ids)

#3
class Dracule:
    def __init__(self, name, blood_level):
        self.name = name
        self.blood_level = blood_level

    def bite(self, targets_blood):
        if self.blood_level >= 100:
            self.blood_level = 100
            print("Вампир сыт")
            return
        self.blood_level += targets_blood

vampire = Dracule("Vampire", 50)
vampire.bite(20)
vampire.bite(25)
vampire.bite(10)
