# Import External Libraries
from PIL import Image
from google_images_download import google_images_download

# Import System Libraries
from os import listdir, remove, makedirs
from os.path import isfile, join, isdir, exists
from shutil import rmtree

from imdb import IMDb
import requests
import shutil
import aiohttp
import asyncio
# Constants
from fileflags import FileFlags as fflags

DEFAULT_LOCATION = './cache/cover_downloads/'
DEFAULT_SMALL_POSTER = '{0}_{1}-Poster_200x272'
DEFAULT_BIG_POSTER = '{0}_{1}-Poster_400x544'


# big_image = DEFAULT_BIG_POSTER.format(clean_title, decoded_search_type)
# small_image = DEFAULT_SMALL_POSTER.format(clean_title, decoded_search_type)

class CoverDownloader:
    def __init__(self):
        self.name = self.__class__.__name__
        self.location = DEFAULT_LOCATION
        self._setup_cache_folder()

    def _setup_cache_folder(self):
        if not exists(self.location):
            makedirs(self.location)

    @staticmethod
    def decode_search_type(search_type):
        if search_type == fflags.ANIME_DIRECTORY_FLAG:
            return 'Anime'
        elif search_type == fflags.SHOW_DIRECTORY_FLAG:
            return 'Show'
        elif search_type == fflags.FILM_DIRECTORY_FLAG:
            return 'Film'
        return ''

    @staticmethod
    def _get_poster(title):
        imdb = IMDb()
        movie_index = imdb.search_movie(title)[0].movieID
        movie_data = imdb.get_movie(str(movie_index))
        print(movie_data['cover'])
        original_cover_uri = movie_data['cover'].split('@')
        return original_cover_uri[0] + '@._V1_.png'
        # return movie_data['cover']

    @staticmethod
    def save_image(file_name, x=200, y=272):
        try:
            # Resizing the image for the poster box size
            img_temp = Image.open(file_name)
            img_temp = img_temp.resize((x, y), Image.ANTIALIAS)
            # Save the resized file to the cache path
            img_temp.save(file_name, img_temp.format)
        except Exception as err:
            print(err)
            return False

        finally:
            return True

    def download(self, websearch, file_path=None):
        if file_path is None:
            file_path = self.location

        clean_title = websearch.title.replace(':', '')
        decoded_search_type = self.decode_search_type(websearch.search_type)
        keywords = '{0}_{1}_Poster'.format(clean_title, decoded_search_type)

        _new_image_path = file_path + keywords + '/' + keywords + '.png'
        print(_new_image_path)
        movie_cover_url = self._get_poster(clean_title)
        print(movie_cover_url)

        if not isdir(file_path + keywords + '/'):
            makedirs(file_path + keywords + '/')

        try:
            assert (not isfile(_new_image_path))
            response = requests.get(movie_cover_url, stream=True)
            # assert (response.status_code == 200)
            with open(_new_image_path, 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
                self.save_image(_new_image_path)
            return _new_image_path
        except AssertionError as assertion_err:
            print(assertion_err)

        except Exception as err:
            print(self.name, ' ', err)
            return './interface/resources/placeholders/poster_placeholder.png'

    def clear_cache(self):
        try:
            if isdir(self.location):
                rmtree(self.location)
        except Exception as err:
            print(self.name, 'Clear Cache Error: ', err)
