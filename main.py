from Class.User import User
import uuid
from CRUD.UsersCRUD import *

list_users = []

delete_user('As63f8vEQaZVnhMpnnCI')

for user in list_users:
    print(user.get_id(), " ", user.get_name(), " ", user.get_first_name())