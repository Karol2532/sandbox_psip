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






for user in users_list:
    print(f'Twój znajomy {user["name"]} dodał {user["posts"]} postów')
