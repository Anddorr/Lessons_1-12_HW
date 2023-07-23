def append_client():
    client_name = input("Enter client's name:")
    print(f'Free rooms: {free_rooms}')
    client_room = int(input("Please choose free room: "))
    free_rooms.remove(client_room)
    busy_rooms.append(client_room)
    clients[client_name] = client_room


def delite_client():
    client_name = input("Enter client's name, that you want delite: ")
    room = clients[client_name]
    busy_rooms.remove(room)
    free_rooms.append(room)


def see_busy_rooms():
    print(f'Busy rooms: {busy_rooms}')


free_rooms = [i for i in range(1, 21)]
busy_rooms = []
clients = {}

print('Wellcome to our Hotel')
while True:
    print('\nActions: take a number(1), release the number(2), see busy rooms(3) ')
    action = input('Chose action: ')
    if action == '1':
        append_client()
    elif action == '2':
        delite_client()
    elif action == '3':
        see_busy_rooms()
