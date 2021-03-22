import requests
import pprint

def insert_token(type):
    with open('C:\my\\tok.txt') as file:
        if type == 'YD':
            return (file.read().splitlines()[0])
        elif type == 'VK':
            return (file.read().splitlines()[1])
        else:
            return f'Неверный тип токена: {type}'

def get_path(file):
    check = f'{os.getcwd()}\{file}'
    if os.path.exists(check):
        return check
    else:
        return 'Ошибка фаил не найден'


def getgroups_vk(iduser):
    print(iduser)
    param = {
        'access_token':insert_token('VK'),
        'v': '5.130',
        'user_id': '644850263',
        'extended': '1',
        'count': '5'
    }
    method_name = 'groups.get'
    url = f"https://api.vk.com/method/{method_name}"
    resp = requests.get(url, params=param)
    return resp.json()


def getalbum_vk(iduser):
    print('getalbum', iduser)
    param = {
        'access_token': insert_token('K'),
        'v': '5.130',
        'owner_id': iduser,
       # 'count': '5'
    }
    method_name = 'photos.getAlbums'
    url = f"https://api.vk.com/method/{method_name}"
    resp_album = requests.get(url, params=param)
    return (resp_album.json())


#pprint(getgroups_vk('644850263'))
print(getalbum_vk("begemot_korovin"))