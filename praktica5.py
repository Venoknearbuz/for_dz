#1
TAXES = 0.13 #константа Налоговая ставка = 13%
year_income_count = float(input("Введите свой годовой доход(одно число)"))

TAXES_count = float(year_income_count * TAXES)
on_hand = float(year_income_count - TAXES_count)

print(f"Общая сумма дохода {year_income_count:.2f}р")
print(f"Сумма рассчитанного налога {TAXES_count:.2f}р")
print(f"На руки будет {on_hand:.2f}р")

#2
kg, m = map(float, input("Введите свой вес и рост (кг, м):").split())

IMT = float(kg / ( m * m ) )
if m>5:
    print("Не верю, что вы больше пяти метров")
else:
    print(f"Ваш индекс массы тела:{IMT:.1f}")

#3
USD_TO_RUB = 95.50

def convert_usd_to_rub(amount_usd):
    """
    Переводит доллары в рубли
    Args:
        amount_usd (float): сумма в долларах
    Returns:
        float: сумма в рублях
    """

    rub = float(amount_usd * USD_TO_RUB)
    return rub

amount_usd= float(input("Введите свою сумму в долларах"))

amount_rub = convert_usd_to_rub(amount_usd)

print(f"Будет {amount_rub} рублей")

#4
PI=3.14

def calculate_rectangle_area(width, height):
    """
    Вычисляет площадь прямоугольника

    Args:
        width(float): ширина
        height(float): высота
    Returns:
        float: площадь прямоугольника
    """

    rectangle_area = float(width * height)
    return rectangle_area

def calculate_circle_area(radius):
    """
    Вычисляет площадь круга

    Args:
        radius(float): радиус круга
        PI(float): число пи, константа
    Returns:
        float: площадь круга

    """

    circle_area = float(PI * radius ** 2)
    return circle_area

width , height = map(float, input("Введите стороны прямоугольника (ширина, высота):").split())
rectangle_perimetr = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника булет {rectangle_perimetr:.2f}")

radius = float(input("Введите радиус окружности"))
circle_perimetr = calculate_circle_area(radius)
print(f"Площадь окружности будет {circle_perimetr:.2f}")

#5
R5000 = 5000
R2000 = 2000
R1000 = 1000
R500 = 500
R200 = 200
R100 = 100

amount = int(input("Введите количество денег которое хотите снять(кратно 100): "))

r5000 = amount//5000
rest = amount%5000
r2000 = rest//2000
rest = rest%2000
r1000 = rest//1000
rest = rest%1000
r500 = rest//500
rest = rest%500
r200 = rest//200
rest = rest%200
r100 = rest//100

print(f"Если вы снимете - {amouey} руб. вы получите купюр: "
      f"\nкупюр по 5000 -{r5000}\nкупюр по 2000 - {r2000}\nкупюр по 1000 -{r1000}"
      f"\nкупюр по 500 - {r500}\nкупюр по 200 - {r200}\nкупюр по 100 - {r100}"

#6
import math

def calculate_distance(x1, y1, x2, y2):
    """
    Вычисляет расстояние между точками
    Args:
        x1, y1 (float): первая точка
        x2, y2 (float): вторая точка
    Returns:
        float: расстояние между точками
    """
    distance = math.sqrt( ( (x1 - x2 )** 2 ) + ( (y1 - y2) **2 ) )
    return distance

def calculate_triangle_area(a,b,c):

    """
    Args:
        a(float): первая сторона
        b(float): вторая сторона
        c(float): третья сторона

    Returns:
        float: площадь триугольника
    """
    p = (a + b + c) / 2
    area= math.sqrt( p * (p - a) * (p - b) * (p - c) )
    return area

x1, y1 = map(int, input("Первая точка (x1 y1): ").split())
x2, y2 = map(int, input("Вторая точка (x2 y2): ").split())

a = calculate_distance(x1,y1,x2,y2)
b = calculate_distance(x1,y1,x2,y2)
c = calculate_distance(x1,y1,x2,y2)

triangle_area = calculate_triangle_area(a,b,c)

print(f"Площадь триугольника будет {triangle_area:.2f}")

#7
C = 49.5
def calculate_drivin_on_taxi(distance, liters):
    """
    Высчитывает сколько литров потрачено и какая стоимость за проезд
    Arg:
        distance(float): дистанция в километрах
        liters(float): литры на 100 км
    Returns:
        float: сколько всего литров потрачено и какая стоимость проезда
    """
    total_liters = distance * (liters/100)
    total_cost = total_liters * C
    return total_liters, total_cost

distance =float(input("Сколько километров проехало такси?"))
liters =float(input("Сколько машина тратит литров за 100 км?"))

t_liters, t_cost = calculate_drivin_on_taxi(distance, liters)
print(f"Потрачено {t_liters}, стоимость {t_cost} рублей")
