
class DbUsers:
    def __init__(self):
        self.all_users = {}

    def add_user(self, email, username, password, address):
        try:
            self.all_users[username]
        except KeyError:
            self.all_users[username] = [email, username, password, address]
            return '{} successfully signed up.'.format(username)

        return 'Username already exits, please choose another'

    def get_user_info(self, username):
        try:
            return self.all_users[username]
        except KeyError:
            return "User not found."

    def get_all_users(self):
        return self.all_users

    def remove_user(self, username):
        try:
            del self.all_users[username]
        except KeyError:
            return '{} does not exits.'.format(username)


class DbCaterers(DbUsers):
    def __init__(self):
        super().__init__()

    def add_user(self, email, username, password, address, category='caterer'):
        try:
            self.all_users[username]
        except KeyError:
            self.all_users[username] = [email, username, password, address, category]
            return '{} created.'.format(username)

        return 'Username already exits, please choose another'