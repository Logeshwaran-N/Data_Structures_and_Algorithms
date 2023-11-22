class Users():
    def __init__(self,username,name,mail,age):
        self.username=username
        self.name=name
        self.mail=mail
        self.age=age
    def __repr__(self):
        return (f'User {self.username} {self.name} {self.age} {self.mail}')
    def __str__(self):
        return self.__repr__()


class UserDB():
    def __init__(self):
        self.users = []

    def insert(self, user):
        self.users.append(user)

    def find(self, username):
        for item in self.users:
            if username == item.username:
                return item

    def update(self, get_user_detail):
        item_to_update = self.find(get_user_detail.username)
        item_to_update.name, item_to_update.mail = get_user_detail.name, get_user_detail.mail


logesh=Users('logeshw','logeshwaran','logwn@g.com',23)
kavi=Users('kavina','kavinb','kavi@g.com',24)
gok=Users('robo','gokushan','gokushan@g.co',25)

all_users=[logesh,kavi,gok]

all_users_db=UserDB()
second_db=UserDB()

all_users_db.insert(user=logesh)
all_users_db.insert(gok)
second_db.insert(kavi)
second_db.insert(logesh)

all_users_db.update(Users(username='logeshww',name='logeshwaran',mail='logesh.wn@g.co',age=23))

print(all_users_db.users)