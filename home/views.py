from django.shortcuts import render
import pyrebase

config={
  "apiKey": "AIzaSyAg4GfFJm73HfeGuEa_2zLF71AiL0_oqLM",
  "authDomain": "test-b38fa.firebaseapp.com",
  "databaseURL": "https://test-b38fa-default-rtdb.firebaseio.com",
  "projectId": "test-b38fa",
  "storageBucket": "test-b38fa.appspot.com",
  "messagingSenderId": "693214188565",
  "appId": "1:693214188565:web:d49ebc4df85569e7fe2a1c"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


# Create your views here.
def Home(request):
    channel_name = database.child('DHT11').child('Humidity').get().val()
    channel_type = database.child('DHT11').child('Temperature').get().val()
    return render(request, 'home.html', 
        {"channel_name" : channel_name,
        "channel_type" : channel_type,})