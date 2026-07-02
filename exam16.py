#2
items_dict = {
    "Меч": 150,
    "Щит": 80,
    "Шлем": 120,
    "Кольцо": 250,
    "Сапоги": 90
}

print("Все предметы в словаре:")
for key in items_dict.keys():
    print("-", key)
    
print("\nВсе стоимости:")
for value in items_dict.values():
    print("-", value)

most_expensive_item = max(items_dict, key=items_dict.get)
max_price = items_dict[most_expensive_item]

print(f"\nСамый дорогой предмет: {most_expensive_item} (стоимость: {max_price})")

#3
class VampireHunter:
    def __init__(self, name, ammo):
        self.name = name
        self.ammo = ammo

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f"{self.name} сделал выстрел! Осталось патронов: {self.ammo}")
        else:
            print("Патроны закончились")


hunter = VampireHunter("Блейд", 2)
hunter.shoot()
hunter.shoot() 
hunter.shoot()
