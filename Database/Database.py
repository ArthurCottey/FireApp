import firebase_admin
from firebase_admin import credentials, firestore

def database():
    cred = credentials.Certificate("Database/fir-app-2a5cd-firebase-adminsdk-opycx-67c2eb2a65.json")
    firebase_admin.initialize_app(cred)
    return firestore.client()