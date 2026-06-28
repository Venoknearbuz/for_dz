#1
x1, y1 = map(int, input("Координаты 1-й клетки: ").split())
x2, y2 = map(int, input("Координаты 2-й клетки: ").split())
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")

#2
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three = data[:3]
print("Первая тройка:", first_three)
last_three = data[-3:]
print("Последняя тройка:", last_three)
reversed_data = data[::-1]
print("В обратном порядке:", reversed_data)
odd_indices = data[1::2]
print("С нечетными индексами:", odd_indices)

#3
class Zombie:
    def __init__(self, health: int, speed: int):
        self.health = health
        self.speed = speed

    def take_damage(self, damage: int):
        if self.health <= 0:
            print("Зомби окончательно мертв и больше не может получать урон.")
            return
        self.health -= damage
        if self.health <= 0:
            print("Зомби окончательно мертв")


zombie = Zombie(health=50, speed=5)
zombie.take_damage(20)
zombie.take_damage(35) 
zombie.take_damage(10)  
