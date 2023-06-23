import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate


api_key: str = os.getenv('YT_API_KEY')


class Channel:
    """Класс для ютуб-канала"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id  #id канала
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.content = None
        self.info = None
        self.title = None
        self.description = None
        self.url = "https://www.youtube.com/channel/" + channel_id  # ссылка на канал

        pass

    def my_channel_id(self):
        return self.channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале.
         just touch set_info and print self.info"""
        self.info = json.dumps(self.content, indent=2, ensure_ascii=False)
        return self.info
