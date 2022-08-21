import csv
courses = ('I', 'II', 'III', 'IV')
from search import *

def cr():
    global courses
    print('Выберите курс: ')
    count = 1
    for i in courses:
        print(f'{count}. {i}')
        count += 1
    user = input()
    while int(user) > count or int(user) < 1:
        print('Такого числа нет в списке!')
        user = input('Попробуйте ещё раз: ')
    course = courses[user - 1]
    return course

def pr_fac():
    with open('faculties.csv', encoding='utf-8') as fac:
        file = csv.reader(fac, delimiter=';')
        count = 0
        for row in file:
            if count != 0:
                print(row[1])
            else:
                count += 1


def pr_stud_poln():
    with open('students.csv', encoding='utf-8') as stud:
        file = csv.reader(stud, delimiter=';')
        for row in file:
            if count != 0:
                print(*row)
            else:
                count += 1


def pr_stud_course(cr):
    course = cr()
    with open('students.csv', encoding='utf-8') as stud:
        file = csv.reader(stud, delimiter=';')
        for row in file:
            if row[5] == course:
                print(row[1])


def pr_stud_course_fac():
    course = cr()
    print('Выберите номер факультета: ')
    pr_fac()
    user = input()
    with open('faculties.csv', encoding='utf-8') as fac:
        file = csv.reader(fac, delimiter=';')
        for row in file:
            if row[0] == user:
                user_fac = row[1]
                break
    with open('students.csv', encoding='utf-8') as stud:
        file = csv.reader(stud, delimiter=';')
        for row in file:
            if row[5] == course and row[4] == user_fac:
                print(row[1])


def pr_stud_fac():
    print('Выберите номер факультета: ')
    pr_fac()
    user = input()
    with open('faculties.csv', encoding='utf-8') as fac:
        file = csv.reader(fac, delimiter=';')
        for row in file:
            if row[0] == user:
                user_fac = row[1]
                break
    with open('students.csv', encoding='utf-8') as stud:
        for row in file:
            if row[4] == user_fac:
                print(row[1])

