import requests

class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _upload_link(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # print(response.status_code)
        return response.json()

    def upload(self, path_to_file):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self._upload_link(path_to_file=path_to_file)
        url = href.get('href')
        # print(f'ссылка для загрузки файла {url}')
        response = requests.put(url, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        # print(response.status_code)
        if response.status_code == 201:
            print(f'Файл {path_to_file} успешно загружен на Яндекс Диск\n')
        else:
            print(f'Ошибка загрузки файла {response.status_code}\nРабота программы остановлена\n')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя

    path_to_file = 'PD_79_Mikhayloff_2.txt'
    token = "y0_AgAAAAAAUzO7AADLWwAAAADgU2u6YHDfksgdT-SrIGZJI_yRlvjFopA"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)