from Database.Database import database
from Class.User import User

def addUser(user):
    db = database()
    db.collection('users').add({
        'id': user.get_id(),
        'firstName': user.get_first_name(),
        'name': user.get_name(),
        'dateOfBirth': user.get_birth_date()
    })