#1
a = 42
b = 3.14159
c = "Hello, Python!"
d= True
e = [1,2,3]
f=(4, 5, 6)
g= {"name":"Alice","age":30}
h = {7,8,9}
i = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

#2.1
my_list = [1,2,3]
#Меняем 1 на 100
my_list[0]=100
print(my_list)

#2.2
my_tuple = (1,2,3)
#Пробуем поменять 1 на 100
#my_tuple[0]=100
#Выдает ошибку TypeError, т.к. кортеж не поддерживает действие замены
print(my_tuple)
#2.3
my_string=["cat"]
#Пробуем поменять "cat" на 'b'
#my_string[0]='b'
#Выдает ошибку TypeError. Текстовый тип не поддерживает такой метод замены
#хватаем слова в квадратные скобки, чтобы сделать переменную в список
my_string[0]=["b"]
print(my_string)

#3
try:
    input("Выберите числа")
    num1= input("первое число?")
    num2= input("второе число?")
    num1 = int(num1)
    num2 = int(num2)
    num3= num1+num2
    print(num3)
except ValueError:
    print("НУЖНЫ ЦЕЛЫЕ ЧИСЛА")
  
#5
shopping_list=['молоко','колбаса','сыр', 'яйца', 'яйца']
shopping_list.append('масло')
print(shopping_list)

unique_items={'молоко','колбаса','сыр', 'яйца', 'яйца'}
print(unique_items)

#6
name = input("Ваше имя: ")
age_str = input("Ваш возраст: ")
subjects_str = input("Любимые предметы (через запятую): ")

age = int(age_str)
subjects = subjects_str.split(",")

student = {"name": name,"age": age,"subjects": subjects}

print("=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)

print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Любимые предметы: {', '.join(student['subjects'])}")

print("=" * 30)
