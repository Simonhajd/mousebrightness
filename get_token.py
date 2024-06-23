import requests
import tkinter as tk
import os
from auth2 import get_auth_code_and_state
import base64
import schedule
import time


def verify_token(access_token, refresh_token):

    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    grant_type = 'refresh_token'
   
    body = {"grant_type": grant_type, "refresh_token": refresh_token, "client_id": client_id}
    headerauth = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic " + base64.b64encode((client_id + ":" + client_secret).encode()).decode()}
    r = requests.post("https://accounts.spotify.com/api/token", data=body, headers=headerauth)
    #print(r.json())
    access_token = r.json()["access_token"]

    return access_token
access_token = os.getenv('ACCESS_TOKEN')
refresh_token = os.getenv('REFRESH_TOKEN')

verify_token(access_token, refresh_token)
def get_token():
    code, state = get_auth_code_and_state()
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    redirect_uri = 'http://localhost:8888/callback'
    code = code
    scope = 'user-read-private user-read-email'
    state = state
    
    print("Code: ", code, "\n\n", "State: ", state)
    body = {"grant_type": "authorization_code", "code": code, "redirect_uri": "https://apple.com"}
    headerauth = {"Authorization": "Basic " + base64.b64encode((client_id + ":" + client_secret).encode()).decode(),
              "Content-Type": "application/x-www-form-urlencoded"}

    r = requests.post("https://accounts.spotify.com/api/token", headers=headerauth, data=body)

    #print(r.json())
    access_token = r.json()["access_token"]
    refresh_token = r.json()["refresh_token"]

    return access_token, refresh_token

    
    
