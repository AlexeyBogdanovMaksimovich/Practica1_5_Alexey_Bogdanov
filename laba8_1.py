#Богданов Алексей Максимович_Ум-222
#Практическая работа 8. Вариант 4 (1)

n = int(input("Введите количество строк массива: "))
m = int(input("Введите количество столбцов массива: "))
A=[]
for i in range(n):
    B=[]
    for j in range(m):
        print("[",i+1,"][",j+1,"] ", end='')
        B.append(int(input("Введите элемент массива: ")))
    A.append(B)

print("---------------------------------------------------------")
print("Введённый массив:")

for i in range(n):
    for j in range(m):
        print(A[i][j], end='\t')
    print()

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

print("---------------------------------------------------------")
print("Строка массива с максимальной суммой: ")
for i in range(1):
    for j in range(m):
        print(A[fl_max][j], end ='\t')
print("; Сумма строки = ", summx)

i = fl_min

print("---------------------------------------------------------")
print("Строка массива с минимальной суммой: ")
for i in range(1):
    for j in range(m):
        print(A[fl_min][j], end ='\t')
print("; Сумма строки = ", summn)


