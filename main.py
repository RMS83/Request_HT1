from pprint import pprint
import requests as requests
import os
import yandex as yandex

class YaUploader:

    def get_token(self):
        with open('token.txt', 'r', encoding='utf-8') as file_:
            return file_.readline().strip('\n')

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.get_token()}'}

    def _get_file_url(self, file_name):
        url_ = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': file_name, 'overwrite': 'true'}
        headers = self.get_headers()
        resp = requests.get(url_, headers=headers, params=params)
        return resp.json()['href']

    def upload_file(self, file_name):
        href = self._get_file_url(file_name)
        print(href)
        data = open(file_name, 'rb')
        resp = requests.put(href, data)
        resp.raise_for_status()
        if resp.status_code == 201:
            print(f'* {file_name} - Загрузка выполнена')

if __name__ == '__main__':
    ya = YaUploader()
    ya.upload_file('upload_file.txt')
