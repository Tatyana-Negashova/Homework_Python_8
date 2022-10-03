import pandas as pd

print('----'*40)
print('Информация о классах')

class_card = {
        'Предмет': ['Русский язык','Алгебра','Обществознание','Биология','История'],
        'Номер парты' : ['1','2','3','4','5','6'],
        'Ряд': ['Первый ряд','Второй ряд','Третий ряд'],
        'ID ученика' : ['01','02','03','04','05','06']
}
  
cc = pd.DataFrame(data = class_card)

with open('cabinet.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{cc}')
        cl.write('\n')
    
print(cc)