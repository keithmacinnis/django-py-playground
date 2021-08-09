# HttpResponse is used to
# pass the information 
# back to view
from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint
import pyrebase
import os


ENV_FB_authDomain = os.environ.get('REACT_APP_authDomain')
ENV_FB_databaseURL = os.environ.get('REACT_APP_databaseURL')
ENV_FB_apiKey = os.environ.get("REACT_APP_apiKey")
ENV_FB_projectId = os.environ.get("REACT_APP_projectId")
ENV_FB_storageBucket = os.environ.get("REACT_APP_storageBucket")
ENV_FB_messagingSenderId = os.environ.get("REACT_APP_messagingSenderId")
ENV_FB_appId = os.environ.get("REACT_APP_appId")

config={
    "authDomain": ENV_FB_authDomain,
    "databaseURL": ENV_FB_databaseURL,
    "apiKey": ENV_FB_apiKey,
    "projectId": ENV_FB_projectId,
    "storageBucket": ENV_FB_storageBucket,
    "messagingSenderId": ENV_FB_messagingSenderId,
    "appId": ENV_FB_appId
}

firebase = pyrebase.initialize_app(config)
authRef = firebase.auth()
databaseRef = firebase.database()

def home (request) :
    activities = databaseRef.child('activities').get().val()
    pprint(activities, sort_dicts=False)
    # This will return Hello Geeks
    # string as HttpResponse
    return render(request, 'home.html', {'activities': activities})
