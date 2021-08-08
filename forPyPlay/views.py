# HttpResponse is used to
# pass the information 
# back to view
from django.http import HttpResponse
import pyrebase
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
config={
    "apiKey": os.getenv('ENV_FB_authDomain'),
    "authDomain": os.getenv('ENV_FB_databaseURL'),
    "databaseURL": os.getenv('ENV_FB_apiKey'),
    "projectId": os.getenv('ENV_FB_projectId'),
    "storageBucket": os.getenv('ENV_FB_storageBucket'),
    "messagingSenderId": os.getenv('ENV_FB_messagingSenderId'),
    "appId": os.getenv('ENV_FB_appId')
}
print("In views.py: ")
print(config)

print(os.getenv('ENV_FB_authDomain'))
# firebase = pyrebase.initialize_app(config)
# authRef = firebase.auth()
# databaseRef = firebase.database()
# Defining a function which
# will receive request and
# perform task depending 
# upon function definition
def home (request) :
    #activity = databaseRef.child('activities').get().val()
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("activity")