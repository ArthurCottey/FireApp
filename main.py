from Class.User import User
import uuid
from CRUD.UsersCRUD import *

list_users = get_users()

print("Avant suppression")
for user in list_users:
    print("User info : ",user.get_name()," ",user.get_first_name()," ",user.get_birth_date())


print("Suppression")
for user in list_users:
    if user.get_id() == 'fu58WJo0MTiDxrDU299Y':
        print("User info : ",user.get_name()," ",user.get_first_name()," ",user.get_birth_date())
        delete_users(user)

print("Après suppression")
for user in list_users:
    print("User info : ",user.get_id(),user.get_name()," ",user.get_first_name()," ",user.get_birth_date())