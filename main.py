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

add_user_to(users_list)
add_user_to(users_list)

for user in users_list:
    print(f'Twój znajomy {user["name"]} dodał {user["posts"]} postów')
