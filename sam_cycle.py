#1
for i in range(2,20):
    if i % 2 == 0:
        print(i)
    else:
        continue

#2
n,m = map(int, input("Введите два числа").split())
for i in range(n,m):
    if m<n:
        for k in range(m,n):
            print(k)
    else:
        print(i)

  #4
  m,n=map(int,input("Введите два числа").split())

for i in range(m,n):
    if m<=n:
        continue
    elif i % 17:
        continue
    elif i % 10 == 9:
        continue
    elif i % 3 == 0 or i % 5 == 0:
        print(i)
    else:
        print("Не удовлетворяет условию")

  #?
  import math
n = int(input("Введите число:"))
fac = 1
for i in range(2, n + 1):
    fac = int(math.factorial * i)
    print(f"БУДЕТ {fac} фактораил")
