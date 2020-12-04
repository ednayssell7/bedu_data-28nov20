#tarea: usando conocimientos de python y request crear un bot para consultar los followers de un usuario de github
#despues descargar el avatar de cada follower 

import requests

#constants

base_url = 'https://api.github.com/'

#functions

def get_github_user(username):
    url = f'{base_url}users/{username}/followers'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def consult_users_followers(followers_url, username):
    response = request.get(followers_url)
    if response.status_code == 200:
        response_content = response.content
        filename = f'tmp/{username}/followers.csv'
        with open(filename, 'wb') as csv_file:
            csv_file.write(response_content)
            return filename
    return None

def download_github_user_avatar(avatar_url, username):
    response = requests.get(avatar_url)
    if response.status_code == 200:
        #download a file from internet
        response_content = response.content
        filename = f'tmp/{username}.png'
        with open(filename, 'wb') as image:
            image.write(response_content)
            return filename
    return None

username = input('Give a github usarname to check his/her followers:\t')
user = get_github_user(username)
get_followers = consult_users_followers(user['followers_url'], username)
filename = download_github_user_avatar(user['avatar_url'], username)
print(filename)