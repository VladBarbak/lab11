"""
Дан текстовий файл f, елементами якого є символи. Записати в файл g ті компоненти файлу f, які є числами, а в файл
h - буквами.
Barbak Vladuslav 122V
"""
while True:
    f=open('f.txt', 'w')
    list=([input("Введіть елемент: ") for i in range(int(input("Скільки чисел ви хочите ввести? ")))])
    f.write(''.join(map(str,list)))
    f=open('f.txt', 'r')
    x=f.read()
    f.close()

    letters=[]
    numbers=[]

    for i in x:
        if i.isalpha():
            letters.append(i)
        if i.isnumeric():
            numbers.append(i)

    g=open('g.txt', 'w')
    g.write(' '.join(map(str,numbers)))
    g.close()

    h=open('h.txt', 'w')
    h.write(' '.join(map(str,letters)))
    h.close()

    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break