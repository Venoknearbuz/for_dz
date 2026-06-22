#1
print("ПРОВЕРКА ЗДОРОВЬЯ")
temp , pressure , rythm = map(int,input("Введите вашу температуру (в цельсиях), давление (верхнее) и пульс (удары в минуты):").split())

if (36 <= temp <= 37) and (110 <= pressure <= 130) and (60 <= rythm <= 100):
    print(f"Темпратура - {temp}, давление - {pressure}, пульс - {rythm}. У вас всё в порядке.")
elif (35 <= temp <= 36) or (37 <= temp <=38) and (105 <= pressure <= 110) or (130 <= pressure <= 140) and (55 < rythm <= 60) or (100 <= rythm <= 110):
    print(f"Темпратура - {temp}, давление - {pressure}, пульс - {rythm}. У вас легкое недомогание")
elif (temp < 35 or temp > 38) or (pressure < 105 or pressure > 140) or (rythm < 55 or rythm >110):
    print(f"Темпратура - {temp}, давление - {pressure}, пульс - {rythm}. ИДИТЕ К ВРАЧУ.")
else:
    print("Я не придумала. Допустим ошибка бип бип")

#2
g = 1
r = 2
b = 3
spot = 0
print("КОЛЕСОООООО")
number = int(input("ВВЕДИТЕ КАРМАНЧИК КОЛЕСИКА(от 0 до 36)"))
if number < 0 or number > 36:
    print("ОШИБКА")
else:
    if number == 0:
        spot = g
    elif (1 <= number <= 10 or 19 <= number <= 28) and number%2 == 0:
        spot = b
    elif (11 <= number <= 18 or 29 <= number < 36) and number%2 == 0:
        spot = r
    else:
        if (1 <= number <= 10 or 19 <= number <= 28) and number%2 != 0:
            spot = r
        elif (11 <= number <= 18 or 29 <= number < 36) and number%2 != 0:
            spot = b
        else:
            print("Ошибка")

if spot == g:
    print("У вас зеленый")
elif spot == r:
    print("У вас красный")
elif spot == b:
    print("У вас черный")
else:
    print("Цифра не должна быть меньше нуля или больше 36")

#3
CHESSBOARD_SIZE = 8
x1, x2, y1, y2 = map(int,input("Введите координаты двух клеток (x1,x2,y1,y2)").split())

if (x1 or x2 or y1 or y2) >= CHESSBOARD_SIZE:
    print("Ошибкаа")
elif (x1 or x2 or y1 or y2) <= 0:
    print("ошибкааа")
else:
    if (x1 %2 == 0) and (y1 %2 == 0):
        spot1 = 1
    elif (x1 %2 != 0) and (y1 %2 != 0):
        spot1 = 1
    else:
        spot1 = 0

    if (x2 %2 == 0) and (y2 %2 == 0):
        spot2 = 1
    elif (x2 %2 != 0) and (y2 %2 != 0):
        spot2 = 1
    else:
        spot2 = 0

    if spot1 == spot2:
        print("YES!")
    else:
        print("NO!")

#4
CHESSBOARD_SIZE = 8

print("ход слоном")

start1, start2 = map(int,input("Введите начальные координаты слона (x1,y1)").split())
end1, end2 = map(int,input("Введите конечне координаты слона (x2,y2)").split())

if (start1 or start2 or end1 or end2) >= CHESSBOARD_SIZE:
    print("Ошибкаа")
elif (start1 or start2 or end1 or end2) <= 0:
    print("ошибкааа")
else:
    if (start1 - end1) == (start2 - end2) or (start1 - end1) == (end2 - start2) and start1 != end1 and start2 != end2:
        print("YES")
    else:
        print("Nuh uh")

#5
#Задача 5
CHESSBOARD_SIZE = 8

print("ход ферзем")

start1, start2 = map(int,input("Введите начальные координаты слона (x1,y1)").split())
end1, end2 = map(int,input("Введите конечне координаты слона (x2,y2)").split())

if (start1 or start2 or end1 or end2) >= CHESSBOARD_SIZE:
    print("Ошибкаа")
elif (start1 or start2 or end1 or end2) <= 0:
    print("ошибкааа")
else:
    if ((start1 - end1) == (start2 - end2) or (start1 - end1) == (end2 - start2) and start1 != end1 and start2 != end2) or (start1 == end1 or start2 == end2):
        print("YES")
    else:
        print("Nuh uh")
