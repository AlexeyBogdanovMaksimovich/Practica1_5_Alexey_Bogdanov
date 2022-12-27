#Богданов Алексей Максимович_Ум-222
#Практическая работа 14, задача №4

f = open('StudentsPerformance 14.csv')

sum = 0
for line in f:
    info = line.split(',')
    if info[1] == '"group C"':
        if info[4] == '"completed"':
            sum+=1
print()
print("Кол-во абитуриентов, относящихся к этнической группе С, закончили подготовительные курсы:", sum)
f.close()


