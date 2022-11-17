# Богданов Алексей Максимович
# Практическая работа 5. Вариант 4.
s=str(input('Введите строку: '))
string=''
k=0
for i in range(len(s)):
    if s[i]!='a':
        string+=s[i]
    else: string+='о'
for i in range(len(string)):
    if string[i]=='о':
        k+=1
print('Все буквы <а> в строке заменены на <о>: ',string)
print('Количество совершенных замен = ',k)
print('Количество символов в строке: ',len(s))
