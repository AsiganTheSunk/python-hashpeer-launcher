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

from colorama import init, Fore
color_scheme = {
    'fst_color': Fore.LIGHTBLUE_EX,
    'snd_color': '',
    'failure': {'text': 'FAILURE', 'color': Fore.LIGHTRED_EX },
    'querying': {'text': 'QUERYNG', 'color': Fore.LIGHTYELLOW_EX },
    'success': {'text': 'SUCCESS', 'color': Fore.LIGHTGREEN_EX }
}


init()

from tracker_endpoint_checker import TrackerEndPointChecker

def launch():
    proxy_pool_manager = TrackerEndPointChecker()
    tracker_end_points = proxy_pool_manager.run()
    trackers = ['ExtraTorrent', 'KickassTorrent', 'MejorTorrent', 'ThePirateBay']


    for index, tracker_end_point in enumerate(tracker_end_points):
        accepted_end_points = []
        rejected_end_points = []
        for data in tracker_end_point:
            if data['status'] == 200:
                accepted_end_points.append(data['end_point'])
            else:
                rejected_end_points.append(data['end_point'])

        # print('  >> {0} - [ Accepted ({1}) | Rejected ({2}) ]'.format(
        #     trackers[index], str(len(accepted_end_points)), str(len(rejected_end_points))))

        # if accepted_end_points:
        #     # print('\n   >> {0}: \n - [ Accepted ({1}) ]'.format(trackers[index], str(len(accepted_end_points))))
        #     print('-------' * 10)
        #     for item in accepted_end_points:
        #         print(item[:-len(tracker_end_points_list[str(trackers[index])]['dummy_search'])])
        #
        # if rejected_end_points:
        #    # print('   >> {0}: \n - [ Rejected ] Tracker EndPoints {1}'.format(trackers[index], str(len(rejected_end_points))))
        #     print('-------' * 10)
        #     for item in rejected_end_points:
        #         print(item[:-len(tracker_end_points_list[str(trackers[index])]['dummy_search'])])


if __name__ == '__main__':
    launch()

