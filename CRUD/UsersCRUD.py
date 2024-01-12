from Database.Database import database
from Class.User import User

def add_user(first_name, name, birth_date):
    db = database()
    data_add = db.collection('users').add({
        'firstName': first_name,
        'name': name,
        'dateOfBirth': birth_date
    })
    user_create = User(data_add[1].id, first_name, name, birth_date)
    return user_create



