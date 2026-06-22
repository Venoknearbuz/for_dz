#1
import math
x=input("введите число")
x=float(x)

y=math.floor(x)+math.ceil(x)

print(y)

#2
import math
x1=input("введите x первой точки")
y1=input("введите y первой точки")
x2=input("введите x второй точки")
y2=input("введите y второй точки")

x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)

p=float(math.sqrt( (x1-x2)**2 + (y1-y2)**2 ) )

print(p)

#3
number=input("введите четырехзначное число")
number=int(number)

if 1000<=number<=9999:
    chislo1=number//1000
    chislo2=(number//100)%10
    chislo3=(number//10)%10
    chislo4=number%10

    print(f"Цифра в позиции тысяч равна {chislo1}")
    print(f"Цифра в позиции сотен равна {chislo2}")
    print(f"Цифра в позиции десятков равна {chislo3}")
    print(f"Цифра в позиции единиц равна {chislo4}")
else:
    print("Покороче или подлинее пожалуйтса")

#4
n=input("Сколько всего школьников?")
k=input("Сколько всего мандаринов?")
n=int(n)
k=int(k)

mand=int(k/n)
kor=int(k%n)

print(f"Одному школьнику достанеться {mand} мандаринов")
print(f"Всего в корзине останеться {kor} мандаринов")

#5
min=input("введите кол.во минут")
min=int(min)
hour =(min//60)
min2=(min%60)

print(f"{min} мин - это {hour} часa и {min2} минут")

#6
import math
x=input("введите значение")
x=int(x)
x=math.radians(x)
tangx=math.tan(x)
tang2x=tangx**2

f=(math.sin(x)+math.cos(x)+tang2x)
f2=int(math.degrees(f))

print(f"будет {f2} градусов")

#7
#Попробывала это решить листом, не знаю, правильно это или нет

mesto=input("введите своё место")
mesto=int(mesto)

kupe1=[1,2,3,4]
kupe2=[5,6,7,8]
kupe3=[9,10,11,12]
kupe4=[13,14,15,16]
kupe5=[17,18,19,20]
kupe6=[21,22,23,24]
kupe7=[25,26,27,28]
kupe8=[29,30,31,32]
kupe9=[33,34,35,36]

if mesto in kupe1:print("вам в первое купе")
elif mesto in kupe2:print("вам в второе купе")
elif mesto in kupe3:print("вам в третье купе")
elif mesto in kupe4:print("вам в четвертое купе")
elif mesto in kupe5:print("вам в пятое купе")
elif mesto in kupe6:print("вам в шестое купе")
elif mesto in kupe7:print("вам в седьмое купе")
elif mesto in kupe8:print("вам в восьмое купе")
elif mesto in kupe9:print("вам в девятое купе")
else: print("идите в другой вагон")
