#!/usr/bin/python3

#
import os


class ReportEngine():
    def __init__(self):
        self.name = self.__class__.__name__
        try:
            os.remove('./curlstem/plugins/plugin_shodan/report/shodan_device_report.txt')
        except OSError:
            pass

    def write_device_report(self, device_instance):
        with open('./curlstem/plugins/plugin_shodan/report/shodan_device_report.txt', 'a') as out:
            out.write('===============' * 5)
            out.write(str(device_instance))
            out.write('===============' * 5)
            out.write('\n')
