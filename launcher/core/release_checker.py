#!/usr/bin/env python3

import asyncio
from aiohttp import ClientSession, TCPConnector, request
from pkg_resources import parse_version

# Import External Libraries
from bs4 import BeautifulSoup

class ReleaseManager:
    def __init__(self):
        self.name = self.__class__.__name__

    async def fetch(self, session, release_page):
        try:
            async with session.request("GET", release_page, allow_redirects=False) as response:
                return await response.text('utf-8')
        except Exception as err:
            print(err)
            return True

    async def get_releases(self):
        async with ClientSession() as session:
            html = await self.fetch(session, 'https://github.com/AsiganTheSunk/python-torrent-scraper/tags')
            return html

    def check_updates(self):
        versions = []
        link_versions = []

        try:
            loop = asyncio.get_event_loop()
            content = loop.run_until_complete(self.get_releases())

            soup = BeautifulSoup(str(content), 'html.parser')
            fst_div = soup.findAll('div', {'class': 'repository-content'})
            snd_div = fst_div[0].findAll('div', {'class': 'Box'})
            thrd_div = snd_div[0].findAll('div', {'class': 'Box-row position-relative d-flex'})

            for each_div in thrd_div:
                data = each_div.findAll('h4', {'class': 'flex-auto min-width-0 pr-2 pb-1 commit-title'})[0]
                versions.append(data.findAll('a')[0].get_text().strip())
                link_versions.append(data.findAll('a')[0]['href'].strip())

            current_release_link = link_versions[0]
            current_release_version = versions[0][1:]

            current_local_version = '0.5.9'
            if parse_version(current_release_version) > parse_version(current_local_version):
                print('[ Current Version ]: {0}'.format(current_local_version))
                print(' (+) New Version Avaliable at [ https://github.com{0} ]'.format(current_release_link))
            else:
                print('[ Current Version ]: {0}'.format(current_local_version))
                print(' (*) Current Version {0}'.format(current_local_version) + ' your System is Up to Date!')
            return True
        except Exception as err:
            return False
