from Class.User import User
import uuid
from CRUD.UsersCRUD import *

list_users = []

list_users.append(add_user("COTTEY", "Baptiste", "14/12/1995"))

print(list_users[0].get_id()," ",list_users[0].get_name()," ",list_users[0].get_first_name()," ",list_users[0].get_birth_date())