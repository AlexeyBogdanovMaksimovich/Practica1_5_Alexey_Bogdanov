#Богданов Алексей Максимович_Ум-222
#Практическая работа 9. Вариант 4 (1)

#Запись матрицы в файл
file = open('BogdanovAlexeyMaksimovich_Um222_Vvod.txt', 'w')

a = int(input("Введите количество строк массива: "))
file.write(str(a) + ' ')
b = int(input("Введите количество столбцов массива: "))
file.write(str(b) + ' ')
flagg=0
c = 0
while flagg<a*b:
    c=int(input("Введите элемент массива: "))
    file.write(str(c) + ' ')
    flagg+=1

file.close()
file = open('BogdanovAlexeyMaksimovich_Um222_Vvod.txt', 'r')

#Считывание значений с файла

klv=0
l=0
D=file.read()
D3=[]
while l!=len(D):
    D2 = []
    while D[l]!=' ':
        D2+=D[l]
        l+=1
    klv+=1

    if klv==1:
        result = ''.join(D2)
        n=int(result)
    else:
        if klv==2:
            result = ''.join(D2)
            m=int(result)
        else:
            if klv>=3:
                result = ''.join(D2)
                D3.append(int(result))
    l += 1

A=[]
g=0

#Запись, считанной с файла матрицы в массив A[]

for i in range(n):
    B=[]
    for j in range(m):
        B.append(D3[g])
        g+=1
    A.append(B)

file.close()

#Запись результатов работы программы в новый файл
file = open('BogdanovAlexeyMaksimovich_Um222_Vivod.txt', 'w')

file.write("---------------------------------------------------------\n")
file.write("Введённый массив:\n")

for i in range(n):
    for j in range(m):
        file.write(str(A[i][j]) + '\t')
    file.write('\n')

#Нахождение строк с минимальной и маскимальной суммой элементов

summx = 0
summn = 0
max2 = 0
fl_max = 0
fl_min = 0

for i in range(1):
    for j in range(m):
        summx+=A[i][j]
        fl_max = i

summn=summx
fl_min=fl_max

i=1
for i in range(n):
    for j in range(m):
        max2+=A[i][j]
    if max2>summx:
        summx = max2
        fl_max = i
    if max2<summn:
        summn = max2
        fl_min = i
    max2 = 0

i = fl_max

file.write("---------------------------------------------------------\n")
file.write("Строка массива с максимальной суммой: ")
for i in range(1):
    for j in range(m):
        file.write(str(A[fl_max][j]) + '\t')
file.write("; Сумма строки = " + str(summx) + '\n')

i = fl_min

file.write("---------------------------------------------------------\n")
file.write("Строка массива с минимальной суммой: ")
for i in range(1):
    for j in range(m):
        file.write(str(A[fl_min][j]) + '\t')
file.write("; Сумма строки = " + str(summn))
file.close()
print()
print("Программа выполнила работу, все результаты в файлах!")
