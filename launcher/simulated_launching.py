from beautiful_tty import ConsoleUtils
from beautiful_launcher import BeautifulLauncher
from core.nt.network_connectivity import NetworkConnectivity
from core.release_checker import ReleaseManager
from constants.placer_holder_headers import hashper_header
from colorama import Fore, Style
import time
from tracker_endpoint_checker import TrackerEndPointChecker
import threading

blauncher = BeautifulLauncher()
tracker_endpoint_checker = TrackerEndPointChecker()


def run_tracker():
    blauncher.print_summary('Validating Tracker EndPoint Pools')
    blauncher.update_checker(launch)


def launch():
    tracker_endpoint_checker.run()


def check_network():
    network_connectivity = NetworkConnectivity()
    network_connectivity.check_status()


def check_releases():
    _check_releases = ReleaseManager()
    _check_releases.check_updates()


def sleeping_process():
    time.sleep(.5)


if __name__ == '__main__':
    console_utils = ConsoleUtils()
    console_utils.hide_cursor()
    console_utils.clear()
    blauncher.print_header(header=hashper_header, _version='0.6.0.0a')

    jobs = {'jobs': [{'job_name': 'Starting Launcher', 'job': check_releases},
                     {'job_name': 'Checking Connectivity', 'job': check_network},
                     {'job_name': 'Checking for Releases', 'job': check_releases},
                     {'job_name': 'Checking Tracker EndPoints', 'job': run_tracker},
                     {'job_name': 'Setting Up Tor Resources', 'job': sleeping_process},
                     {'job_name': 'Checking Connectivity with Tor Resources', 'job': sleeping_process},
                     {'job_name': 'Setting Up VPN Resources Launcher', 'job': sleeping_process},
                     {'job_name': 'Checking Connectivity with VPN Resources', 'job': sleeping_process},
                     {'job_name': 'Setting Up Tor Through VPN Resources', 'job': sleeping_process},
                     {'job_name': 'Checking Connectivity with Tor Through VPN', 'job': sleeping_process},
                     {'job_name': 'Launching Hashpeer GUI', 'job': sleeping_process},
    ]}

    for _index, item in enumerate(jobs['jobs']):
        time.sleep(.5)
        if _index > 0:
            print('\033[1A\r', flush=True, end='')
            print(blauncher.format_job_text(jobs['jobs'][_index - 1]['job_name']), flush=True)
            print(blauncher.current_job_text(item['job_name']), flush=True)
            job = threading.Thread(target=jobs['jobs'][_index]['job'])
            job.start()
            job.join()
        else:
            print(blauncher.current_job_text(item['job_name']), flush=True)

        # TODO Move to a proper clean up method, add lenth of the list being displayed to measure the cleaning surface.
        if _index == 3:
            print('\033[7A\r', flush=True, end='')
            for i in range(0, 8, 1):
                print(' ' * 100, flush=True)
            print('\033[8A\r', flush=True, end='')
    print()





