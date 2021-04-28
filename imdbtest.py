import requests
import urllib.parse
from fileflags import FileFlags as fflags
from websearch_instance import WebSearchInstance
from cover_downloader import CoverDownloader
from imdb import IMDb
from threading import Timer
from time import sleep


# pattern = 'http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q={movie_title}'
# url = pattern.format(movie_title=urllib.parse.quote(title))
# print(url)
# r = requests.get(url)
# res = r.json()
# # sections in descending order or preference
# for section in ['popular', 'exact', 'substring']:
#     key = 'title_' + section
#     if key in res:
#         return res[key][0]['id']


def search_similar_imdb(keyword):
    """ return IMDB id for search string

        Args::
            title (str): the movie title search string

        Returns:
            str. IMDB id, e.g., 'tt0095016'
            None. If no match was found

    """
    imdb_py = IMDb()
    similar_titles = imdb_py.search_movie(keyword)

    return [titles['title'] for titles in similar_titles]

# if __name__ == "__main__":
#     test_movie_title = 'Kong vs'
#     # websearch = WebSearchInstance(title=test_movie_title, year='2017', search_type=fflags.FILM_FLAG)
#     #
#     # _cd = CoverDownloader()
#     # _cd.download(websearch)
#     search_similar_imdb(test_movie_title)
#
#     while True:
#         try:
#             print('SCAN BARCODE')
#             userInput = raw_input()
#             # doing something with input
#         except:
#     # run this while there is no input

from threading import Thread
import time

thread_running = True


def my_forever_while():
    global thread_running

    start_time = time.time()

    # run this while there is no input
    while thread_running:
        time.sleep(0.1)

        if time.time() - start_time >= 5:
            start_time = time.time()
            # print('Another 5 seconds has passed')


def take_input():
    user_input = input('Type user input: ')
    # doing something with the input
    # print('The user input is: ', user_input)
    data = search_similar_imdb(user_input)
    print(list(set(data)))


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def hello(name):
    print("Hello %s!" % name)


if __name__ == '__main__':
    # print("starting...")
    # search_input = 'Mortal Kombat'
    # rt = RepeatedTimer(5, search_similar_imdb, search_input)  # it auto-starts, no need of rt.start()
    # try:
    #     # rt.start()
    #     sleep(5)  # your long-running job goes here...
    # finally:
    #     rt.stop()  # better in a try/finally block to make sure the program ends!

    while True:
        t1 = Thread(target=my_forever_while)
        t2 = Thread(target=take_input)

        t1.start()
        t2.start()

        t2.join()  # interpreter will wait until your process get completed or terminated
    # thread_running = False
    #     print('The end')
