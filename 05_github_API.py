import requests

#constants

base_url = 'https://api.github.com/'

#functions

def get_github_user(username):
    url = f'{base_url}users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
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

username = input('Give a github usarname:\t')
user = get_github_user(username)
filename = download_github_user_avatar(user['avatar_url'], username)
print(filename)



