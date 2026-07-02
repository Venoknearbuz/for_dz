#1
cost = int(input("Введите стоимость услуги ведьмака: "))
coins = [25, 10, 5, 1]
total_coins = 0

for coin in coins:
    count = cost // coin
    total_coins += count

    cost %= coin

print("Минимальное количество монет:", total_coins)

#2
line1 = "192.168.1.1 10.0.0.1 172.16.0.1"
line2 = "10.0.0.1 192.168.1.2 172.16.0.1"
line3 = "172.16.0.1 8.8.8.8 192.168.1.1"

set1 = set(line1.split())
set2 = set(line2.split())
set3 = set(line3.split())

all_ips = set1.union(set2, set3)
common_ips = set1.intersection(set2, set3)
result = all_ips - common_ips

print("Искомые IP-адреса:", list(result))

#3
class Potion:
    def __init__(self, uses_left):
        self.uses_left = uses_left

    def drink(self):
        if self.uses_left > 0:
            self.uses_left -= 1
            print("Здоровье восстановлено")
        else:
            print("Пустая фляга")


healing_potion = Potion(2)
healing_potion.drink()
healing_potion.drink()
healing_potion.drink()
