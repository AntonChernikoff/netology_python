from pprint import pprint
import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, save_path='netology', overwrite=True):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {"path": save_path, "overwrite": overwrite}
        result = requests.get(f'{URL}/upload', headers=headers, params=params).json()
        pprint(result)
        responce = requests.put(result['href'], data=open(file_path, 'rb'))
        responce.raise_for_status()
        if responce.status_code == 201:
            print("Загрузка выполнена")
        else:
            print(f"Ошибка при загрузке файла! = {responce.status_code}")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    PATH_MAIN = os.getcwd()
    file_name = '1.txt'
    path_to_file = os.path.join(PATH_MAIN,'netology_python','files_txt',file_name)
    TOKEN = ''
    uploader = YaUploader(TOKEN)
    result = uploader.upload(path_to_file,file_name)
    # print(result)



    