import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate

# api_key: str = os.getenv('YT_API_KEY')  Это не работало
api_key: str = 'AIzaSyAT2fssSmUegKbhed6Yt9hkBfV0IKVnELo'  # то что сгенерировал API гугла. А это работает


class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id  # id канала
        self.channel = self.youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        self.subscriber_count: int = self.channel['items'][0]['statistics']['subscriberCount']  # количество подписчиков
        self.video_count = self.channel['items'][0]['statistics']['videoCount']  # количество видео
        self.viewCount = self.channel['items'][0]['statistics']['viewCount']  # общее количество просмотров
        self.title: str = self.channel['items'][0]['snippet']['title']  # Название канала
        self.description: str = self.channel['items'][0]['snippet']['description']  # Описание канала
        self.url = "https://www.youtube.com/channel/" + channel_id  # ссылка на канал

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    @property
    def channel_id(self):
        # print(self.channel_id)
        return self._channel_id

    # @channel_id.setter
    # def channel_id(self, value):
    #     self._channel_id = value
    def print_info(self):
        """Выводит в консоль информацию о канале."""
        self.channel = self.youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        self.chan = self.channel
        self.info = json.dumps(self.channel, indent=2, ensure_ascii=False)
        # print(self.channel['items'][0]['snippet'])
        print(f"Название канала: {self.title}, Описание канала {self.description}, ссылка на канал: "
              f"{self.url}, количество подписчиков {self.subscriber_count}, id канала: {self._channel_id}, "
              f"количество видео: {self.video_count}, общее количество просмотров: {self.viewCount}")

    def to_json(self, filename):
        """Метод `to_json()`, сохраняющий в файл значения атрибутов экземпляра Channel"""

        data = {'channel_id': self._channel_id,
                'channel': self.channel,
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subscriberCount': self.subscriber_count,
                'video_count': self.video_count,
                'viewCount': self.viewCount
                }
        with open(filename, 'w') as f:
            json.dump(data, f, )

    @classmethod
    def get_service(cls):
        """Класс-метод `get_service()`, возвращающий объект для работы с YouTube API"""
        return cls.youtube
