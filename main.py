from Class.User import User
import uuid
from CRUD.UsersCRUD import *

#region Main program
list_users = []
list_users = get_users()
for user in list_users:
    print(user.get_name()," ",user.get_first_name())
#endregion