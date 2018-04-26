
class DbUsers:
    def __init__(self):
        self.all_users = dict()
        self.all_emails = list()
        self.id = 1

    def add_user(self, email, username, password, address):
        if email not in self.all_emails:
            try:
                self.all_users[username]
            except KeyError:
                self.all_users[username] = dict(email=email, username=username, password=password,
                                                address=address, id=self.id)
                self.all_emails.append(email)
                return True

            else:
                self.id +=1
                return False

        return False

    def get_user(self, username):
        try:
            return self.all_users[username]
        except KeyError:
            pass
        return False

    def get_all_users(self):
        return self.all_users

    def remove_user(self, username):
        try:
            del self.all_users[username]
        except KeyError:
            return False
        else:
            return True


class DbCaterers(DbUsers):
    def __init__(self):
        super().__init__()

    def add_user(self, email, username, password, address, category='caterer', brand_name=''):
        if email not in self.all_emails:
            try:
                self.all_users[username]
            except KeyError:
                brand_name_final = brand_name if brand_name else username
                self.all_users[username] = dict(email=email, username=username, password=password, address=address,
                                                category=category, brand_name=brand_name_final)
                self.all_emails.append(email)
                return True

        return False


class DbMeals:
    def __init__(self):
        self.meals = dict()
        # self.id

    def add_meal(self, caterer, meal_name, price):
        try:
            self.meals[caterer]
        except KeyError:
            meals = list()
            meal_id = 1
            meal = [meal_id, meal_name, price]
            meals.append(meal)

            self.meals[caterer] = meals
            # self.id += 1
            return True

        else:
            all_meals = self.meals[caterer]
            meal_id = all_meals[-1][0] + 1
            all_meals.append([meal_id, meal_name, price])

        # for any reason meal not added
        return False

    def get_all_meals(self, caterer):
        return self.meals[caterer]

