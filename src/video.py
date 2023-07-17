import json

import src

from src.channel import Channel


class Video():

    def __init__(self, video_id):
        """
        Инициализация атрибутов класса + дополнительный
        защищенный атрибут video_data в котором все данные
        **Если введено неверное ID видео, обрабатываем ошибку
        IndexError, все поля кроме video_id выставляем в None
        """
        self.video_id = video_id
        try:
            self.__video_data = src.channel.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                                  id=video_id).execute()
            self.title = self.__video_data["items"][0]["snippet"]["title"]
            self.video_link = f'https://www.youtube.com/watch?v={video_id}'
            self.view_count = self.__video_data["items"][0]["statistics"]["viewCount"]
            self.like_count = self.__video_data["items"][0]["statistics"]["likeCount"]

        except IndexError:
            self.__video_data = None
            self.title = None
            self.video_link = None
            self.view_count = None
            self.like_count = None


# Объявляем дочерний от Video класс PLVideo
class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        """
        Инициализация атрибутов класса + дополнительный
        защищенный атрибут playlist_data в котором все данные
        """
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.__playlist_data = src.channel.youtube.playlistItems().list(playlistId=playlist_id,
                                                                        part='contentDetails,snippet',
                                                                        maxResults=50,
                                                                        ).execute()
