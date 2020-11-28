import requests

#constants

base_url = 'https://api.github.com/'

#response = requests.get(base_url)
#print(response)

#functions

def get_github_user(username):
    url = f'{base_url}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

username = input('Give a github usarname:\t')
user = get_github_user(username)
print(user)


