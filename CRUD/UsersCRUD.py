from Database.Database import database
from Class.User import User

def add_user(first_name, name):
    db = database()
    data_add = db.collection('users').add({
        'firstName': first_name.upper(),
        'name': name.capitalize()
    })
    user_create = User(data_add[1].id, first_name, name)
    return user_create



