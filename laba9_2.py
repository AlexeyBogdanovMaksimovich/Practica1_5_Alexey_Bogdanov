#Богданов Алексей Максимович_Ум-222
#Практическая работа 9. Вариант 4 (2)

#Запись матрицы в файл
file = open('BogdanovAlexeyMaksimovich_Um222_Vvod.txt', 'w')

a = int(input("Введите количество строк и стобцов массива: "))
file.write(str(a) + ' ')
flagg=0
c = 0
while flagg<a*a:
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
        if klv>=2:
            result = ''.join(D2)
            D3.append(int(result))
    l += 1

A=[]
g=0

#Запись, считанной с файла матрицы в массив A[]

for i in range(n):
    B=[]
    for j in range(n):
        B.append(D3[g])
        g+=1
    A.append(B)

file.close()

#Запись результатов работы программы в новый файл
file = open('BogdanovAlexeyMaksimovich_Um222_Vivod.txt', 'w')

file.write("---------------------------------------------------------\n")
file.write("Введённый массив:\n")

for i in range(n):
    for j in range(n):
        file.write(str(A[i][j]) + '\t')
    file.write('\n')

#Заменяем отрицательные элементы на нули, а положительные на единицы

C=[]
for i in range(n):
    B=[]
    for j in range(n):
        if A[i][j]<0:
            A[i][j]=0
            B.append(A[i][j])
        else:
            if A[i][j]>0:
                A[i][j] = 1
                B.append(A[i][j])
            else:
                B.append(A[i][j])
    C.append(B)

#Вывод нижней треугольной матрицы в файл

file.write("---------------------------------------------------------\n")
file.write("Полученный результат(нижняя треугольная матрица от исходной, где отрицательные элементы - нули, а положительные - единицы):\n")
for i in range(n):
    for j in range(n):
        if j<i or i==j:
            file.write(str(C[i][j]) + '\t')
    file.write('\n')
file.close()
print()
print("Программа выполнила работу, все результаты в файлах!")