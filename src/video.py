import os

import src

from src.channel import Channel

from googleapiclient.discovery import build

import googleapiclient.discovery
api_key: str = 'AIzaSyAT2fssSmUegKbhed6Yt9hkBfV0IKVnELo'  # то что сгенерировал API гугла. А это работает
class Video:
    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.api_key: str = 'AIzaSyAT2fssSmUegKbhed6Yt9hkBfV0IKVnELo'
        # создать специальный объект для работы с API
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.video_response = self.youtube.videos().list(part='snippet,statistics', id=video_id).execute()
        self.title = self.video_response['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/channel/' + video_id
        self.view_count = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f'{self.title}'

# Объявляем дочерний от Video класс PLVideo
class PLVideo(Video):
    def __init__(self, video_id, playlist_id) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id
