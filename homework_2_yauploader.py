import requests
import os
import json


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = file_path.split(os.sep)[-1]
        headers = {'Authorization': self.token}
        url1 = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_name, 'overwrite': 'true'}
        response1 = requests.get(url1, params=params, headers=headers)
        data = response1.json()

        url2 = data['href']
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response2 = requests.put(url2, files=files)
        if response2.status_code == 201 or response2.status_code == 200:
            print(f'Файл {file_path} успешно загружен на яндекс диск.')
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('')
    result = uploader.upload(os.path.join(os.getcwd(), 'file_for_upload.txt'))
