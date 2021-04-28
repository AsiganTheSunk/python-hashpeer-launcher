#!/usr/bin/env python3

# path to qClient config C:\Users\Asigan\AppData\Roaming\qBittorrent.ini
# search values, to change and auto configurate. nº of conexions etc etc

from qbittorrent import Client


class QClientManager:
    def __init__(self, url: str = 'http://127.0.0.1:8090/'):
        self.name = self.__class__.__name__
        self.url = url
        # self.user = user
        # self.paswd = paswd

        # Launching Session to QClient
        self.session = Client(self.url)
        self.session.login('admin', 'adminadmin')

    def session_shutdown(self) -> bool:
        try:
            self.session.shutdown()
        except Exception as e:
            print(e)
        return True

    def get_torrent_info(self) -> None:
        torrents = self.session.torrents()
        for torrent_item in torrents:
            print('%s: [%s] \n\t\t- %s' % (self.name, torrent_item['hash'], torrent_item['name']))

    def load_magnet(self, magnet_uri: str) -> bool:
        try:
            self.session.download_from_link(magnet_uri)
        except Exception as e:
            print(e)
        return True
