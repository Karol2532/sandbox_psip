from dane import users_list

# print(nick_of_user)

def update_user(users_list: list[dict,dict]) -> None:
    nick_of_user = input('Podaj nick użytkownika do modyfikacji: ')
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('taki ćwok istnieje')
            user['name'] = input('podaj nowe imię: ')
            user['nick'] = input('Podaj nową ksywę: ')
            user['posts'] = int(input('podaj liczbę postów: '))


update_user(users_list)
for user in users_list:
    print(user)
