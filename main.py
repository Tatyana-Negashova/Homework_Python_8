import student as st
import cabinet as cab

def option():
    choice = int(input('Какую операцию хотите сделать? \n \
    1: Поиск ID студента по фамилии \n \
    2: Узнать класс и место в нём ученика \n \
    3: Выход\n \
    Ваш выбор: '))

    if choice == 1:
        Surname = str(input("Введите фамилию ученика: "))
        if Surname in st.student_card['Фамилия']:
            index = st.student_card['Фамилия'].index(Surname)
        print(f"{st.student_card['ID'][index]}, {st.student_card['Имя'][index]},{st.student_card['Фамилия'][index]}\n,{st.student_card['Дата рождения'][index]}, {st.student_card['Успеваемость'][index]}")
        print('\nХотите выполнить иную операцию? Y или N: ')
        num = input()
        if num == 'Y' or 'y':
            option()
        exit()

    elif choice == 2:
        c = input('Введите ID студента для получения информации: ')
        if c in cab.class_card['ID']:
            index = cab.class_card['ID'].index(c)
            print(f" Сидит в классе - {cab.class_card['Предмет'][index]}, за партой номер - {cab.class_card['Номер парты'][index]}, это {cab.class_card['Ряд'][index]}, Имя: {st.student_card['Имя'][index]}, Фамилия - {st.student_card['Фамилия'][index]}, и успеваемасть у студента: {st.student_card['Успеваемость'][index]}")
            print('\nХотите выполнить иную операцию? Y или N: ')
            num = input()
            if num == 'Y' or 'y':
                option()
            exit()
    else:
        print('Спасибо за обращение. Хорошего дня!')
    exit()
option()