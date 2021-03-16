import os

file_name = '1.txt'

def get_path(file):
    check = f'{os.getcwd()}\{file}'
    if os.path.exists(check):
        return check
    else:
        return 'Ошибка фаил не найден'



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        # Тут ваша логика
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('<Your Yandex Disk token>')
    result = uploader.upload(get_path(file_name))


print(get_path(file_name))