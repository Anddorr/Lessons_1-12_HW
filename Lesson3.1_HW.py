print('Wellcome in contact list\n')


def welcome():  # Функция выбора действия
    print(f'Your contact list: \n{contact_list}')
    print(f'Variants of action: {Actions}')
    global Action
    Action = input('Your action with contact list: ')
    choose_action(Action)


def choose_action(action):  # Функция исполняющая выбранное действие
    if action == '1':
        add_contact = input('Add contact: ')
        contact_list.append(add_contact)
        print(f'Your updated contact list: \n{contact_list}\n')
    elif action == '2':
        old_contact = input('Which contact you want edit: ')
        new_contact = input('Enter new contact: ')
        index = contact_list.index(old_contact)
        contact_list[index] = new_contact
        print(f'Your updated contact list: \n{contact_list}\n')
    elif action == '3':
        delete_contact = input('Which contact you want delete: ')
        contact_list.remove(delete_contact)
        print(f'Your updated contact list: \n{contact_list}\n')
    elif action == '4':
        exit()

    if 'Stop_programm(4)' not in Actions:
        Actions.append('Stop_programm(4)')
    else:
        pass
    welcome()


Actions = ['Add(1)', 'Edit(2)', 'Delete(3)']
contact_list = ['Malika', 'Bob']
Action = ''

welcome()
