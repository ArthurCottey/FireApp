from Database.Database import database
from google.cloud.firestore_v1 import FieldFilter
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

#region Function get_user
def get_user(first_name, name):
    user_list = []
    db = database()
    users = db.collection('users').where(filter=FieldFilter('firstName', '==', first_name)).where(filter=FieldFilter('name', '==', name)).get()
    if not users:
        return False
    else:
        user_data = users[0].to_dict()
        user_list.append(User(users[0].id, user_data['firstName'], user_data['name']))
    return user_list
#endregion

#region Function update_user
def update_user(user_id, first_name, name):
    db = database()
    db.collection('users').document(user_id).update({
        'firstName': first_name.upper(),
        'name': name.capitalize()
    })
    user_update = db.collection('users').document(user_id).get()
    user_data = user_update.to_dict()
    user_updated = User(user_update.id, user_data['firstName'], user_data['name'])
    return user_updated
#endregion