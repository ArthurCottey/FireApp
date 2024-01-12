from Config.config import *
import firebase_admin
from firebase_admin import credentials, firestore
__cred = credentials.Certificate(getFirebasePath())
firebase_admin.initialize_app(__cred)

def database():
    return firestore.client()