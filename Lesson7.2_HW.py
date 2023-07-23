def new_student():
    student_name = input('Enter new student full name: ')
    student_class = int(input('In which class he/she will be study: '))
    School[student_name] = student_class
    print('Student has been registrate')


def remove_student():
    student_name = input('Enter new student full name: ')
    if student_name in School.keys():
        School.pop(student_name)
        print('Student has been remove')
    else:
        print('These Student isn\'t study in our school')


def another_class():
    student_name = input('Enter new student full name: ')
    if student_name in School.keys():
        student_class = int(input('Enter new class where will be study student: '))
        School[student_name] = student_class
    else:
        print('These Student isn\'t study in our school')


School = {}
print('Wellcome in our School! ')
while True:
    action = input('\nChoose action: add, remove, change class\n:')
    if action.lower() == 'add':
        new_student()
    elif action.lower() == 'remove':
        remove_student()
    elif action.lower() == 'change class':
        another_class()
    else:
        print('Undefined action')
