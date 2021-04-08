n = int(input("Введите необходимое количество билетов:\n"))
L = []
c=1
while c != n+1 :
    print(f"Введите возраст посетителя №{c}:")
    age = int(input())
    if age < 18 :
        price = 0
    elif 18 <= age < 25 :
        price = 990
    else :
        price = 1390
    L.append(price)
    c += 1
if len(L)>3:
    print("Общая стоимость ваших билетов:", int(sum(L) / 100 * 90))
else:
    print("Общая стоимость ваших билетов:", sum(L))




