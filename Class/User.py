import uuid

class User:

    def __init__(self, first_name, name, date_of_birth):
        self.id = str(uuid.uuid4())
        self.first_name = first_name
        self.name = name
        self.birth_date = date_of_birth

    def set_id(self, id):
        self.id = id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_name(self, name):
        self.name = name

    def set_birth_date(self, birth_date):
        self.birth_date = birth_date

    def get_id(self):
        return self.id

    def get_first_name(self):
        return self.first_name

    def get_name(self):
        return self.name

    def get_birth_date(self):
        return self.birth_date