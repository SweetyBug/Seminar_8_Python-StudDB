from add import *
from search import *

menu = '*** 1. Добавить студента ***\n' \
       '*** 2. Добавить факультет ***\n' \
       '*** 3. Добавить преподавателя ***\n' \
       '*** 4. Поиск студентов ***\n' \
       '*** 5. Поиск преподавателей ***\n' \
       '*** 6. Показать факультеты ***\n'

menu_stud = '*** 1. Список студентов с полной информацией ***\n' \
            '*** 2. Список студентов по факультету ***\n' \
            '*** 3. Список студентов по курсу ***\n' \
            '*** 4. Список студентов по курсу и факультету ***\n' \
            '*** 5. Список студентов по дате поступления (диапазон) ***\n'

menu_teach = '*** 1. Список преподавателй с полной информацией ***\n' \
             '*** 2. Список преподавателй по предмету ***\n' \
             '*** 3. Список препподавателей по дате трудоустройства (диапазон) ***\n'

def user_view():
    global menu
    global menu_teach
    global menu_stud
    print(f'Что вы сделать? \n {menu}')
    user = input('Ввыберите номер пункта: ')
    if user == '1':
        print(addStudent())
    elif user == '2':
        print(addFaculties())
    elif user == '3':
        print(addTeacher())
    elif user == '4':
        print(f'Что вы хотите ищите? \n {menu_stud}')
        user = input('Ввыберите номер пункта: ')
        if user == '1':
            pr_stud_poln()
        elif user == '2':
            pr_stud_fac()
        elif user == '3':
            pr_stud_course()
        elif user == '4':
            pr_stud_course_fac()
#        elif user == '5':
#           #
#    elif user == '5':
#        print(f'Что вы хотите ищите? \n {menu_stud}')
#        user = input('Ввыберите номер пункта: ')
#        if user == '1':
#            #
#        elif user == '2':
#            #
#        elif user == '3':
#            #
#    elif user == '6':
#        pr_fac()
