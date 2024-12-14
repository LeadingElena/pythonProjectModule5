import re

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    """
    Класс пользователя, содержащий логин и пароль
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password_confirm == password:
            self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Выберите действие:\n1 - войти\n2 - зарегистрироваться\n'))
        if choice == 1:
            login = input('Введите логин: ')
            if login in database.data:
                password = input('Введите пароль: ')
                if password == database.data[login]:
                    print(f'Вход выполнен, {login}')
                else:
                    print('Пароль введен не верный. Повторите вход.')
            else:
                print('Пользователь не найден. Повторите вход')
                
        if choice == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                    password_1 := input('Повторите пароль: '))
            if password != password_1:
                print('Пароли не совпадают.')
                continue
            elif len(password) < 8 or not re.findall(r'\d+', password):
                print('Ошибка! Пароль должен иметь не менее 8 символов и содержать хотя бы одну цифру.')
                continue

        database.add_user(user.username, user.password)
        print(database.data)