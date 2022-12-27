#Богданов Алексей Максимович_Ум-222
#Практическая работа 13

import json
from collections import Counter

#Открытие json
with open ('data.json') as f:
    data=json.load(f)

#Подсчёт количества клиентов, совершивих действие с категорией datepicker
A_data=[]
for item in data['events_data']:
    clnts=item['client_id']
    catg=item['category']
    if catg=='datepicker':
        A_data.append(clnts)

lst=Counter(A_data).keys()
print('Количество уникальных клиентов: ' + str(len(lst)))



