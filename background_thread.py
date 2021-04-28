from daemon_with_states.custom_state import Context
from daemon_with_states.job_state import JobInitialized
from daemon_with_states.task_state import TaskInitialized
from aiomultiprocess import Pool

from fileflags import FileFlags as fflags
from websearch_instance import WebSearchInstance
from cover_downloader import CoverDownloader
# System modules
from queue import Queue
from threading import Thread
import time
import asyncio
from torrentscraper.torrent_scraper import TorrentScraper

test_movie_title = 'Kong: Skull Island'
# test_movie_title = 'Totoro'
websearch = WebSearchInstance(title=test_movie_title, year='2017', search_type=fflags.FILM_DIRECTORY_FLAG)
_cd = CoverDownloader()


def test1():
    task_status = Context(TaskInitialized(), 'Cover IMG')
    task_status.advance()
    _cd.clear_cache()
    task_status.advance()
    img = _cd.download(websearch)
    task_status.advance()
    return img


async def test2():
    task_status = Context(TaskInitialized(), 'Cover IMG')
    task_status.advance()
    _cd.clear_cache()
    task_status.advance()
    img = await _cd.download(websearch)
    task_status.advance()
    return img


jobs = {'jobs': [
    {'job_name': 'Job A0', 'job': test1},
    {'job_name': 'Job B0', 'job': test1},
    {'job_name': 'Job B0', 'job': test1},
    {'job_name': 'Job B0', 'job': test1},
    {'job_name': 'Job B0', 'job': test1},
    {'job_name': 'Job B0', 'job': test1},
]}

jobs2 = {'jobs': [
    {'job_name': 'Job A0', 'job': test2},
    {'job_name': 'Job B0', 'job': test2},
    {'job_name': 'Job B0', 'job': test2},
    {'job_name': 'Job B0', 'job': test2},
    {'job_name': 'Job B0', 'job': test2},
    {'job_name': 'Job B0', 'job': test2},
]}


class BackgroundThread(object):
    def __init__(self):
        self.name = self.__class__.__name__

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    @staticmethod
    async def execute_job(_job):
        return _job['job']()

    async def resolve_pool(self, _jobs, _mode, _priority):
        job_status = Context(JobInitialized(), 'Loading Components')
        job_status.advance()
        async with Pool() as pool:
            result = await pool.map(self.execute_job, jobs['jobs'])
        job_status.advance()
        return result

    def run(self, _jobs_list):
        loop = asyncio.get_event_loop()
        data_point = loop.run_until_complete(self.resolve_pool(_jobs=_jobs_list, _mode=0, _priority=0))
        # data_point = asyncio.run(self.resolve_pool(_jobs=_jobs_list, _mode=0, _priority=0))
        return data_point

    def run_sequential(self, _job_list):
        for _index, item in enumerate(jobs['jobs']):
            job = Thread(target=jobs['jobs'][_index]['job'])
            job.start()
            job.join()


if __name__ == "__main__":
    start_time = time.time()
    with BackgroundThread() as background_thread:
        background_thread.run(jobs)
    print("--- %s seconds ---" % (time.time() - start_time))

    # start_time = time.time()
    # test1()
    # test1()
    # test1()
    # test1()
    # test1()
    # test1()
    # print("--- %s seconds ---" % (time.time() - start_time))

    # start_time = time.time()
    # with BackgroundThread() as background_thread:
    #     background_thread.run_sequential(jobs)
    # print("--- %s seconds ---" % (time.time() - start_time))

    # torrent_scraper = TorrentScraper()
    # torrent_scraper.scraper_engine.search(websearch)

