from Database.Database import database
from Class.User import User

#region Function add_user
def add_user(first_name, name):
    db = database()
    data_add = db.collection('users').add({
        'firstName': first_name.upper(),
        'name': name.capitalize()
    })
    user_create = User(data_add[1].id, first_name, name)
    return user_create
#endregion

#region Function get_users
def get_users():
    list_users = []
    db = database()
    users = db.collection('users').get()
    for user in users:
        user_data = user.to_dict()
        list_users.append(User(user.id, user_data['firstName'], user_data['name']))
    return list_users
#endregion


