import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate


# api_key: str = os.getenv('YT_API_KEY')  Это не работало
api_key: str = 'AIzaSyAT2fssSmUegKbhed6Yt9hkBfV0IKVnELo'   # то что сгенерировал API гугла. А это работает

class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id  #id канала
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']  # количество подписчиков
        self.video_count = self.channel['items'][0]['statistics']['videoCount']  # количество видео
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']  # общее количество просмотров
        self.title: str = self.channel['items'][0]['snippet']['title']   # Название канала
        self.description: str = self.channel['items'][0]['snippet']['description']  # Описание канала
        self.url = "https://www.youtube.com/channel/" + channel_id  # ссылка на канал


    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def my_channel_id(self):
        # print(self.channel_id)
        return self.channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel
