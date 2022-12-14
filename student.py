import pandas as pd 

print('Список учеников:')

student_card = {
        'ID': ['01','02','03','04','05','06'],
        'Имя' : ['Гендальф','Алексей','Анна','Татьяна','Светлана','Мария'],
        'Фамилия': ['Иванов','Морозова','Кургинян','Перова','Достоевский','Молчанова'],
        'Дата рождения': ['05.06.2003','21.09.2004','09.12.2000','17.08.2005','02.06.2001','01.01.2003'],
        'Успеваемость': ['Отличник','Троечник','Хорошист','Отличник','Хорошист','Троечник']
}
    
sc = pd.DataFrame(data = student_card)

with open('students.csv', 'a',encoding='UTF-8') as cl:
        cl.write(f'{sc}')
        cl.write('\n')
    
print(sc)