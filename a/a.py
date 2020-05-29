"""
Дани двійкові файли f та g, компоненти яких є цілими числами. Отримати в файлі h нові компоненти, що утворюються в
результаті віднімання двох компонентів файлів f та g, що знаходяться на відповідних позиціях
Barbak Vladuslav 122V
"""
from random import randint
while True:
    f=open('f.txt', 'wb')
    f.write(bytearray([randint(0,255) for i in range(int(input("Скільки чисел ви хочите ввести ? ")))]))
    f=open('f.txt', 'rb')
    x=f.read()
    f.close()

    g=open('g.txt', 'wb')
    g.write(bytearray([randint(0,255) for j in range(int(input("Скільки чисел ви хочите ввести ? ")))]))
    g=open('g.txt', 'rb')
    y=g.read()
    g.close()

    s1=[]
    s2=[]

    for i in x:
        s1.append(i)
    for j in y:
        s2.append(j)

    print('1-Список:', s1)
    print('2-Список:', s2)

    difference=[a-b for a, b in zip(s1,s2)]
    print('Різниця:', difference)

    h=open('h.txt', 'w')
    h.write(' '.join(map(str,difference)))
    h.close()

    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break