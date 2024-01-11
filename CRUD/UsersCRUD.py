from Database.Database import database
from Class.User import User

def add_user(user):
    db = database()
    db.collection('users').add({
        'id': user.get_id(),
        'firstName': user.get_first_name(),
        'name': user.get_name(),
        'dateOfBirth': user.get_birth_date()
    })

def get_users():
    db = database()
    list_users = []
    collection_users = db.collection('users')
    users = collection_users.get()
    for user in users:
        data = user.to_dict()
        new_user = User(user.id, data.get('firstName'), data.get('name'), data.get('dateOfBirth'))
        list_users.append(new_user)
        del new_user
    return list_users

def delete_users(user):
    db = database()
    collection_users = db.collection('users')
    collection_users.document(user.get_id()).delete()



