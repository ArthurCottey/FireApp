from Class.User import User
import uuid
from CRUD.UsersCRUD import *

add_user(User(str(uuid.uuid4()), 'COTILLON', 'Teddy', '14/02/2007'))

list_users = get_users()

for user in list_users:
    print("User info : ",user.get_name()," ",user.get_first_name()," ",user.get_birth_date())