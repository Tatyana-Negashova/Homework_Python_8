import student_info as si
import cabinet_info as cab

def option():
    choice = int(input('Какую операцию хотите сделать? \n \
    1: Поиск ID студента по фамилии \n \
    2: Узнать класс и место в нём ученика \n \
    3: Выход\n \
    Ваш выбор: '))

    if choice == 1:
        Surname = str(input("Введите фамилию ученика: "))
        if Surname in si.stud_card['Фамилия']:
            index = si.stud_card['Фамилия'].index(Surname)
        print(f"{si.stud_card['ID'][index]}, {si.stud_card['Имя'][index]},{si.stud_card['Фамилия'][index]}\n,{si.stud_card['Дата рождения'][index]}, {si.stud_card['Успеваемость'][index]}")
        print('\nХотите выполнить иную операцию? Y или N: ')
        num = input()
        if num == 'Y' or 'y':
            option()
        exit()

    elif choice == 2:
        c = input('Введите ID студента для получения информации: ')
        if c in cab.class_card['ID']:
            index = cab.class_card['ID'].index(c)
            print(f" Сидит в классе - {cab.class_card['Предмет'][index]}\n\, за партой номер - {cab.class_card['Номер парты'][index]}, это {cab.class_card['Ряд'][index]}, парта - {cab.class_card['Вид парты'][index]}, Имя: {si.stud_card['Имя'][index]}, Фамилия - {si.stud_card['Фамилия'][index]}, и успеваемасть у студента: {si.stud_card['Успеваемость'][index]}")
            print('\nХотите выполнить иную операцию? Y или N: ')
            num = input()
            if num == 'Y' or 'y':
                option()
            exit()
    else:
        print('Выберите ещё раз')
    exit()
option()