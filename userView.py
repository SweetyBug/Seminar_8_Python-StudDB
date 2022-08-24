from add import *
from search import *

menu = '*** 1. Добавить студента ***\n' \
       '*** 2. Добавить факультет ***\n' \
       '*** 3. Добавить преподавателя ***\n' \
       '*** 4. Поиск студентов ***\n' \
       '*** 5. Поиск преподавателей ***\n' \
       '*** 6. Показать факультеты ***\n' \
       '-------------------------------------\n' \
       'Чтобы выйти введите "end"\n'

menu_stud = '*** 1. Список студентов с полной информацией ***\n' \
            '*** 2. Список студентов по факультету ***\n' \
            '*** 3. Список студентов по курсу ***\n' \
            '*** 4. Список студентов по курсу и факультету ***\n'

menu_teach = '*** 1. Список преподавателй с полной информацией ***\n' \
             '*** 2. Список преподавателй по предмету ***\n' \

def user_view():
    global menu
    global menu_teach
    global menu_stud
    print(f'Что вы хотите сделать? \n {menu}')
    user = input('Ввыберите номер пункта: ')
    if user.lower() == 'end':
        end = 'Пока!'
        return end
    elif user == '1':
        print(addStudent())
        user_view()
    elif user == '2':
        print(addFaculties())
        user_view()
    elif user == '3':
        print(addTeacher())
        user_view()
    elif user == '4':
        print(f'Что вы хотите ищите? \n {menu_stud}')
        user = input('Ввыберите номер пункта: ')
        if user == '1':
            pr_stud_poln()
            user_view()
        elif user == '2':
            pr_stud_fac()
            user_view()
        elif user == '3':
            pr_stud_course()
            user_view()
        elif user == '4':
            pr_stud_course_fac()
            user_view()
    elif user == '5':
        print(f'Что вы ищите? \n {menu_teach}')
        user = input('Ввыберите номер пункта: ')
        if user == '1':
            pr_tech_poln()
        elif user == '2':
            pr_tech_les()
    elif user == '6':
        pr_fac()
