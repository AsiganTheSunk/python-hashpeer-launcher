from main import launch
import time
import threading
from colorama import init, Fore, Style
from constants.color_schemes import color_scheme
from constants.placer_holder_headers import loading_dot, loading_bar, hashper_header
from beautiful_tty import ConsoleUtils
# Font Color Configuration
init(autoreset=True)

color_scheme = {
    'fst_color': Fore.LIGHTBLUE_EX,
    'snd_color': '',
    'failure': {'text': 'FAILURE', 'color': Fore.LIGHTRED_EX},
    'querying': {'text': 'QUERYNG', 'color': Fore.LIGHTYELLOW_EX},
    'success': {'text': 'SUCCESS', 'color': Fore.LIGHTGREEN_EX}
}
# trackers = ['ExtraTorrent', 'KickassTorrent', 'MejorTorrent', 'ThePirateBay']
#
# acepted_trackers = ['https://proxtpb.art', 'https://247prox.link', 'https://unblocktheship.org', 'https://proxy247.art']

class BeautifulLauncher:
    def __init__(self):
        self.name = self.__class__.__name__
        self.main_color = color_scheme['fst_color']

    def format_job_text(self, job):
        return Fore.LIGHTBLUE_EX + ' >: [ ' + Fore.RESET + 'Hashpeer' + Fore.LIGHTBLUE_EX + ' ]: ' + Fore.RESET + '{0}'.format(job)

    def current_job_text(self, job):
        return self.format_job_text(self.format_bold_text(job))

    def format_bold_text(self, data):
        return Style.BRIGHT + data

    def format_test(self, color=color_scheme['fst_color']):
        return color + ' >: [ ' + Fore.RESET + 'Hashpeer' + color + ' ]: ' + Fore.RESET + 'Starting Launcher'

    def format_aux(self):
        return self.main_color + ' [ ' + Fore.RESET + '{0}'.format(' / ' + self.main_color + ' ]')

    def format_large_section_brackets(self, data='Validating Tracker EndPoint Pool'):
        return self.main_color + ' [ ' + Fore.RESET + '{0:^64}'.format(data) + self.main_color + ' ]'

    def print_section(self, _data):
        print(self.format_aux() + self.format_large_section_brackets(_data))

    def format_brackets(self, data):
        return self.main_color + ' [ ' + Fore.RESET + '{0}'.format(data) + self.main_color + ' ]'

    def format_centered_brackets(self, data):
        return '{0:^79}'.format(self.format_brackets(data))

    def format_version(self, version):
        return '{0:>30}'.format(' ') + self.format_brackets('Version') + ':' + Fore.RESET + ' {0}'.format(version)

    def format_filler(self, filler, multiplier):
        return self.main_color + ' {0:>79}'.format(filler * multiplier)

    def print_header(self, header, _version, _filler='=', _multiplier=79):
        for header_line in header[:-1]:
            print(self.main_color + '{0}'.format(header_line))

        print(self.main_color + '{0}'.format(header[len(header) - 1:][0] + self.format_version(version=_version)))
        print(self.format_filler(_filler, _multiplier))
        print()

    def print_summary(self, _data, _filler='=', _multiplier=79):
        print()
        print('{0:>20}{1:^45}{2:<20}'.format('Trackers', 'Summary', ' Status'))
        print(self.format_filler(_filler, _multiplier))

    def print_brackets(self, text, sub_text, filler='=', multiplier=79, subheader=False, color=color_scheme['fst_color']):
        print(color + ' [ '.format() + Fore.RESET + ' {0:^78} '.format(text) + color + ' ]:' + Fore.RESET + ' {0} '.format(sub_text) + Fore.LIGHTBLUE_EX)
        if subheader:
            print(Fore.LIGHTBLUE_EX + ' {0}'.format(filler * multiplier) + Fore.LIGHTBLUE_EX)

    def animated_loading(self):
        for char in loading_dot:
            print('\r ' + color_scheme['fst_color'] + '[' + Fore.RESET + '{0:^5}'.format(char) + color_scheme['fst_color'] + ']', end='')
            time.sleep(.150)
        print('\r', flush=True, end='')

    def clear_summary(self, _data):
        from beautiful_tty import ConsoleUtils
        console_utils = ConsoleUtils()

        for index in range(0, _data, 1):
            console_utils.move_up_cursor(index)
            print('\r', flush=True, end='')


    def update_checker(self, _target):
        try:
            the_process = threading.Thread(target=_target)
            the_process.start()

            while the_process.isAlive():
                self.animated_loading()
            print('\r', flush=True, end='')
        except:
            print('Something Went Wrong during Update Period')
#
# def main():
#     blauncher = BeautifulLauncher()
#
#     blauncher.print_header(header=hashper_header, _version='0.0.0a')
#     print()
#     print(Fore.LIGHTBLUE_EX + ' >: [ ' + Fore.RESET + 'Hashpeer' + Fore.LIGHTBLUE_EX + ' ]: ' + Fore.RESET + 'Starting Launcher')
#     print(Fore.LIGHTBLUE_EX + ' >: [ ' + Fore.RESET + 'Hashpeer' + Fore.LIGHTBLUE_EX + ' ]: ' + Fore.RESET + 'Checking Connectivity')
#     print(Fore.LIGHTBLUE_EX + ' >: [ ' + Fore.RESET + 'Hashpeer' + Fore.LIGHTBLUE_EX + ' ]: ' + Fore.RESET + 'Checking for Updates')
#     print(Fore.LIGHTBLUE_EX + ' >: [ ' + Fore.RESET + 'Hashpeer' + Fore.LIGHTBLUE_EX + ' ]: ' + Fore.RESET + 'Checking Tracker EndPoints')
#     print(Fore.LIGHTBLUE_EX + ' >: [ ' + Fore.RESET + 'Hashpeer' + Fore.LIGHTBLUE_EX + ' ]: ' + Fore.RESET + 'Setting Up Tor Circuits')
#     print(Fore.LIGHTBLUE_EX + ' >: [ ' + Fore.RESET + 'Hashpeer' + Fore.LIGHTBLUE_EX + ' ]: ' + Fore.RESET + 'Setting Up VPN')
#     print()
#     print()
#
#
#     # blauncher.print_summary('Validating Tracker EndPoint Pools')
#     # blauncher.update_checker(_target=launch)
#
# class Manager(object):
#     def new_thread(self):
#         return TrackerEndPointManager(parent=self)
#
#     def on_tracker_end_point_checked(self, thread, data):
#         print(thread, data)
#
# class TrackerEndPointManager(threading.Thread):
#     def __init__(self, parent=None):
#         self.parent = parent
#         super(TrackerEndPointManager, self).__init__()
#
#     def run(self):
#         main()
#
# if __name__ == '__main__':
#     console_utils = ConsoleUtils()
#     # console_utils.clear()
#     console_utils.hide_cursor()
#     mgr = Manager()
#     thread = mgr.new_thread()
#     thread.start()
#     # print_summary(trackers)
#     # print_brackets('coco1', 'coco2', subheader=True)
#     # def move(y, x):
#     #     print("\033[%d;%dH" % (y, x))
