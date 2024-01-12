from Config.config import *
import firebase_admin
from firebase_admin import credentials, firestore

#region Firebase initialization
__cred = credentials.Certificate(getFirebasePath())
firebase_admin.initialize_app(__cred)
#endregion

#region Get Firestore client
def database():
    return firestore.client()
#endregion