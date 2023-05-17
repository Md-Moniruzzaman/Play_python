from flask import Flask
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("api/Key.json")
default_app = initialize_app(cred)