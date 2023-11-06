from dane import users_list
def add_user_to(users_list: list) -> None:
    """
    add object to list
    :param users_list: list - user list
    :return: None
    """
    name = input('podaj imię')
    nick = input('podaj nick')
    posts = input('podaj liczbę postów')
    users_list.append({"name": name, "nick": nick, "posts": posts})

#add_user_to(users_list)

def remove_user_from(users_list: list) -> None:
    """
    remove object from list
    :param users_list: list - user list
    :return: None
    """
    tmp_list = []
    name = input('podaj imię użytkownika do usunięcia')
    for user in users_list:
        if user['name'] == name:
            tmp_list.append(user)
    print(f'Znaleziono użytkowników:')
    for numerek, user_to_be_removed in enumerate(tmp_list):
        print(f'{numerek+1}: {user_to_be_removed}')
    print('0: usuń wszystkich znalezionych użytkowników')
    numer = int(input(f'wybierz użytkownika do usunięcia:'))
    if numer == 0:
        for user in tmp_list:
            users_list.remove(user)
    else:
        users_list.remove(tmp_list[numer - 1])

def show_users_from(users_list: list)-> None:
    for user in users_list:
        print(f'Twój znajomy {user["name"]} dodał {user["posts"]} postów')


def gui() -> None:
    while True:
        print(f'Witaj na WATbooku \n'
              f'0: Zamknij serwis \n'
              f'1: Wyświetl użytkowników \n'
              f'2: Dodaj użytkownika \n'
              f'3: Usuń użytkownika \n'
              f'4: Edytuj użytkownika')

        menu_option = input('Wybierz funkcję do wykonania')
        print(f'Wybrano funkcję {menu_option}')

        match menu_option:
            case '0':
                print('Zamykam serwis')
                break
            case '1':
                print('Wyświetlanie listy użytkowników')
                show_users_from(users_list)
            case '2':
                print('Dodawanie użytkownika')
                add_user_to(users_list)
            case '3':
                print('Usuwanie użytkownika')
                remove_user_from(users_list)
            case '4':
                print('Edytowanie użytkownika')
                print('Jeszcze ni mom')