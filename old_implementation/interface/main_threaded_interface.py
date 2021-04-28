#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import External Libraries
from tkinter import *
# Import Custom Frames
from old_implementation.interface.component.result_frame.result_main_frame import ResultMainFrame
# Import System Libraries
import threading
import queue
import os


class TkinterDaemon:
    def __init__(self, master):
        self.name = self.__class__.__name__

        self.master = master

        # Create the queue
        self.queue = queue.Queue()

        # Set up the GUI part
        # self.gui = InputMainFrame(master, 0, 0, self.retrieveData, self.queue)
        # self.result_gui = None
        # Set up the thread to do asynchronous I/O
        # More threads can also be created and used, if necessary
        # self.active_search = 0
        # Start the periodic call in the GUI to check if the queue contains
        # anything

        self.periodicCall()
        self.periodicCallCategory()


    async def daeomn_queue_resolve(self):
        try:
            async with session.request("GET", tracker_end_point, allow_redirects=False) as response:
                await response.text('utf-8')
            return callback(tracker_end_point, response.status)
        except Exception as err:
            return callback(tracker_end_point, 500)
        finally:
            await conn.close()
            await session.close()

    async def fetch_status(self, tracker_end_point):
        async with Pool() as pool:
            result = await pool.map(self.assert_status, tracker_end_point)
        return result

    def periodicCallCategory(self):
        if self.gui.search_type_popup.selection == 'SHOW' or self.gui.search_type_popup.selection == 'SERIE':
            self.gui.year_entry.reset_text()
            self.gui.title_entry.enable()
            self.gui.year_entry.disable()
            self.gui.season_entry.enable()
            self.gui.episode_entry.enable()
            self.gui.category_menu_option['state'] = 'disable'
            self.gui.quality_popup['state'] = 'normal'

        self.master.after(100, self.periodicCallCategory)

    def periodicCall(self):
        '''

        :return:
        '''
        self.gui.processIncoming()
        while self.active_search:
            print('BackgroundThread: ENDED')
            top = Toplevel()
            if os.name == 'nt':
                top.iconbitmap('./interface/resources/grumpy-cat.ico')
            top.resizable(width=False, height=False)

            self.result_gui = ResultMainFrame(top, 0, 0, self.gui.dataframe, self.gui.info, self.gui.image_poster)
            self.gui.search_button['state'] = 'normal'
            self.reset_active_search()
        else:
            self.master.after(100, self.periodicCall)

    def BackgroundThread(self, websearch):
        '''

        :param websearch:
        :return:
        '''
        if not self.active_search:
            self.se_config = CustomConfigParser('./torrentscraper.ini')
            self.scraper_config = self.se_config.get_section_map('ScraperEngine')

            # Asynchronous I/O of Scraper Engine
            self.gui.progressbar_status['text'] = 'Scraping Magnets from Trackers ...'
            torrent_scraper = TorrentScraper(self.scraper_config)
            dataframe = torrent_scraper.scrap(websearch)
            self.queue.put(dataframe)
            self.gui.progressbar['value'] = 60
            self.gui.update_idletasks()

            self.gui.progressbar_status['text'] = 'Retrieving Poster Image ...'
            cover_downloader = CoverResourceProvider()
            cover = cover_downloader.get(websearch)
            self.queue.put(cover)
            self.gui.progressbar['value'] = 80
            self.gui.update_idletasks()

            self.gui.progressbar_status['text'] = 'Retrieving General Information ...'

            summary_provider = SummaryResourceProvider()
            info = summary_provider.get(websearch)
            self.queue.put(info)
            self.gui.progressbar['value'] = 100
            self.gui.progressbar_status['text'] = 'Done !'
            self.gui.update_idletasks()
            self.active_search = 1
            print('Status: ', self.active_search)

    def retrieveData(self, websearch):
        '''

        :param websearch:
        :return:
        '''
        if self.gui.validate_entries():
            print('Scrap!, Status: ', self.active_search)
            self.gui.search_button['state'] = 'disable'
            self.gui.update_idletasks()
            tmp_websearh = websearch.validate()

            thread = threading.Thread(target=self.BackgroundThread, args=(tmp_websearh,))
            thread.start()

    def reset_active_search(self):
        '''
        :return:
        '''
        self.active_search = 0
        self.gui.progressbar['value'] = 0
        self.gui.progressbar_status['text'] = ''
        self.gui.update_idletasks()
        self.gui.image_poster = None
        self.gui.dataframe = None
        self.gui.info = None