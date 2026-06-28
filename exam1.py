#1
def check_health_status(temperature, pressure_sys, pulse):
    temp_abnormal = temperature < 36.0 or temperature > 37.2
    pulse_abnormal = pulse < 60 or pulse > 90
    pressure_abnormal = pressure_sys < 110 or pressure_sys > 130

    if temp_abnormal or pulse_abnormal or pressure_abnormal:
        if (temperature > 38.0) or (pulse > 100 or pulse < 50) or (pressure_sys > 140 or pressure_sys < 90):
            return "Требуется врач"
        else:
            return "Легкое недомогание"
    else:
        return "Нормальное состояние"
try:
    temp = float(input("Введите температуру тела (например, 36.6): "))
    pressure = int(input("Введите верхнее (систолическое) давление (например, 120): "))
    pulse_rate = int(input("Введите пульс (например, 75): "))

    result = check_health_status(temp, pressure, pulse_rate)
    print(f"Предполагаемое состояние здоровья: {result}")
except ValueError:
    print("Пожалуйста, вводите только числовые значения.")
  
#2
ip1_set = set(input("Введите первые три айпи: ").split())
ip2_set = set(input("Введите вторые три айпи: ").split())
ip3_set = set(input("Введите третьи три айпи: ").split())

all_ips = ip1_set | ip2_set | ip3_set
common_ips = ip1_set & ip2_set & ip3_set
result = list(all_ips - common_ips)
result.sort()
print(result)

#для ввода:
#1 192.168.1.1 10.0.0.5 172.16.0.10
#2 10.0.0.5 192.168.1.1 192.168.1.5
#3 172.16.0.10 10.0.0.5 192.168.1.1

#3
class Weapon:
    def __init__(self,name,damage,durability):
        self.name = name
        self.damage = damage
        self.durability = durability
    def attack(self):
        if self.durability <= 0:
            print(f"Оружие {self.name} уже сломано! Атака невозможна.")
            return

        print(f"{self.name} наносит {self.damage}")
        self.durability -= 1

        if self.durability <= 0:
            print(f"{self.name} сломано")

sword = Weapon("Стальной меч", damage=15, durability=2)
for i in range(3):
    sword.attack()
