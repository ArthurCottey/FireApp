from Database.Database import database
from Class.User import User

def add_user(user):
    db = database()
    data_adddb.collection('users').add({
        'firstName': user.get_first_name(),
        'name': user.get_name(),
        'dateOfBirth': user.get_birth_date()
    })




