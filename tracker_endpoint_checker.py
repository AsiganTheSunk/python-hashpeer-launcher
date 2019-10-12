#TODO retrieve proxy endpoints for trackers
# verify 200 OK
# Add them to the list of proxies
# Create a request to test the functionality of the tracker_endpoint
# then generate a file to be read when hashper loads for the first time since close up.
# Preguntar Pelicula Favorita o hacer un listado de 100 resultados +- para evitar lanzar siempre los mismos y que nos
# marquen en un futuro si los sistemas de deteccion mejoran. {'movie_title':'El Viaje de Chihiro','movie_year': '2001'}
# Don't harcode the endpoints for the proxy info, use a ini
# {'tpb': {'proxy_list_endpoint_0': 'https://piratebay-proxylist.se/'}}
# Create a Object with the Scraper function class ProxyListEndpoint()
# _
# from evento import Event
# from bs4 import BeautifulSoup

# Import Modules for Multiprocess + Async Operations
import asyncio
from aiohttp import ClientSession, TCPConnector
from aiomultiprocess import Pool
from colorama import init, Fore
from constants.color_schemes import color_scheme
import time
# Importing Tracker Enpoint Pools
from constants.configuration_file import tracker_end_points_list

init()


def callback_assertion(end_point, status):
    try:
        assert (status == 200)
        return {'end_point': end_point, 'status': status}
    except AssertionError:
        return {'end_point': end_point, 'status': status}


class TrackerEndPointChecker:
    def __init__(self):
        self.name = self.__class__.__name__
        self.number_of_end_points = len(tracker_end_points_list)


    async def assert_status(self, tracker_end_point, callback=callback_assertion):
        # Limit the rate somehow
        conn = TCPConnector(limit_per_host=1)
        session = ClientSession(connector=conn)
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

    def run(self):
        data = []
        print(' ', flush=True, end='')

        for _index, _item in enumerate(tracker_end_points_list):
            if _index == 0:
                print(color_scheme['fst_color'] + '' + Fore.RESET + Fore.YELLOW + '' + color_scheme['fst_color'] + '' + Fore.RESET + ' {0:<24s} '.format(_item) + color_scheme[
                    'fst_color'] + ' {0:<23s} '.format('') + ' [ ' + Fore.RESET + Fore.YELLOW + ' {0:^11s} '.format(
                    'QUERYING') + Fore.RESET + color_scheme[
                          'fst_color'] + ' ]', flush=True)


            else:
                print(color_scheme['fst_color'] + '   (' + Fore.RESET + Fore.YELLOW + '?' + color_scheme['fst_color'] + ')  ' + Fore.RESET + ' {0:<24s} '.format(_item) + color_scheme[
                    'fst_color'] + ' {0:<23s} '.format('') + ' [ ' + Fore.RESET + Fore.YELLOW + ' {0:^11s} '.format(
                    'QUERYING') + Fore.RESET + color_scheme[
                          'fst_color'] + ' ]', flush=True)

        # Asi no casca no tocar omfg
        print('\033[4A\r', flush=True, end='')
        for _index, _item in enumerate(tracker_end_points_list):
            time.sleep(3)
            try:
                aux = [str(tracker_end_point + tracker_end_points_list[_item]['dummy_search']) for tracker_end_point in tracker_end_points_list[_item]['tracker_end_point_list']]

                if _item == 'ThePirateBay':
                    raise Exception

                data_point = asyncio.run(self.fetch_status(aux))
                data.append(data_point)



            except Exception as err:
                print('\r', flush=True, end='')
                print(color_scheme['fst_color'] + '   (' + Fore.RESET + Fore.LIGHTRED_EX + 'x' + color_scheme[
                    'fst_color'] + ')  ' + Fore.RESET + ' {0:<24s} '.format(_item) + color_scheme[
                          'fst_color'] + ' {0:<23s} '.format(
                    '') + ' [ ' + Fore.RESET + Fore.LIGHTRED_EX + ' {0:^11s} '.format(
                    'FAILURE') + Fore.RESET + color_scheme[
                          'fst_color'] + ' ]', flush=True)

            else:
                print('\r', flush=True, end='')
                print(color_scheme['fst_color'] + '   (' + Fore.RESET + Fore.LIGHTGREEN_EX + '+' + color_scheme['fst_color'] + ')  ' + Fore.RESET + ' {0:<24s} '.format(_item) + color_scheme[
                    'fst_color'] + ' {0:<23s} '.format('') + ' [ ' + Fore.RESET + Fore.LIGHTGREEN_EX + ' {0:^11s} '.format(
                    'SUCCESS') + Fore.RESET + color_scheme[
                          'fst_color'] + ' ]', flush=True)

                print('\r', flush=True, end='')
        return data
