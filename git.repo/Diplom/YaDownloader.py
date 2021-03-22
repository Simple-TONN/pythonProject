import os
import requests

file_name = 'test.txt'


def get_path(file):
    check = f'{os.getcwd()}\{file}'
    if os.path.exists(check):
        return check
    else:
        return 'Ошибка фаил не найден'


def insert_token(type):
    with open('C:\my\\tok.txt') as file:
        if type == 'YD':
            return (file.read().splitlines()[0])
        elif type == 'VK':
            return (file.read().splitlines()[1])
        elif type == 'K':
            return (file.read().splitlines()[2])
        else:
            return f'Неверный тип токена: {type}'



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        # Тут ваша логика
        res_get = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                               headers={'Authorization': f'OAuth {self.token}'},
                               params={'path': file_name, 'fields': 'href', 'overwrite': True}, )
        link = res_get.json()['href']
        if res_get.status_code != 200:
            return "Ошибка на этапе получения ссылки"
        else:
            with open(get_path(file_name), 'rb') as file:
                res_put = requests.put(link, files={'file': file})
                if res_put.status_code != 201:
                    return "Ошибка загрузки"
                else:
                    return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader(insert_token())
    result = uploader.upload(get_path(file_name))
    print(result)
