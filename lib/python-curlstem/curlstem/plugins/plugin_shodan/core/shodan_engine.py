#!/usr/bin/python3

#
from curlstem.plugins.plugin_shodan.core.shodan_pandas_engine import PandasEngine
from curlstem.plugins.plugin_shodan.core.shodan_report_engine import ReportEngine
from curlstem.plugins.plugin_shodan.struct_data.shodan_device_instance import DeviceInstance
from curlstem.core.curlstem_proxy_engine import ProxyEngine

#
import shodan

# Imports Custom Logger & Logging Modules
from curlstem.logger.custom_logger import CustomLogger
from logging import DEBUG
import logging

#
from time import sleep
import re


class ShodanEngine():
    def __init__(self, api_key='JDBpL9wKLTIgMhvTJObHIjcY9xovsGA2', logging_lvl=DEBUG):
        self.name = self.__class__.__name__
        self.api_key = api_key

        self.proxy_engine = ProxyEngine()
        self.shodan_api = shodan.Shodan(api_key, self.proxy_engine.get_proxy_address())
        self.report_engine = ReportEngine()

        self.logger = CustomLogger(name=__name__, level=logging_lvl)

        # CustomLogger Format Definition
        formatter = logging.Formatter(fmt='%(asctime)s - [%(levelname)s]: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # Custom Logger File Configuration: File Init Configuration
        file_handler = logging.FileHandler('./curlstem/plugins/plugin_shodan/log/ShodanEngine.log', 'w')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level=logging_lvl)

        # Custom Logger Console Configuration; Console Init Configuration
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging_lvl)

        # Custom Logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def country_filter(self, response, shodan_filters):
        '''

        :param response:
        :param shodan_filters:
        :return:
        '''
        try:
            _filtered_data = []
            
            # Apply Second Filter
            for unfiltered_data in response['matches']:
                _country = unfiltered_data['location']['country_code3']

                if _country == shodan_filters['country']:
                    _filtered_data.append(unfiltered_data)
            return _filtered_data
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))

    def search(self, shodan_filters, query='scada'):
        '''

        :param shodan_filters:
        :param query:
        :return:
        '''

        _organization_list = []
        _transport_list = []
        _city_list = []
        _server_list = []
        _country_code3_list = []
        _latitude_list = []
        _longitude_list = []
        _location_list = []
        _postal_code_list = []
        _data_list = []
        _ip_address_list = []
        _ports_list = []
        _cve_list = []
        _postal_code = []

        _response = self.shodan_api.search(query=query)

        _filtered_data = []

        try:
            self.logger.info('{0} Found [ {1} ] Reported Devices'.format(self.name, _response['total']))
            if shodan_filters['country'] != '':
                self.logger.info('{0} Applying Country Filter ... '.format(self.name))
                _filtered_data = self.country_filter(response=_response, shodan_filters=shodan_filters)

            self.logger.info('{0} Device Count {1} For Query [ {2} ]'.format(self.name, len(_filtered_data),
                                                                             query + ' ' + str(shodan_filters)))

            print('===============' * 5)
            for index, item in enumerate(_filtered_data):
                self.logger.info('Device Number: [ {0} ]'.format(index))
                print('===============' * 5)

                _transport = self.retrieve_transport(item)
                _transport_list.append(_transport)

                _ip_address = self.retrieve_ip_address(item)
                _ip_address_list.append(_ip_address)

                _ports = self.retrieve_ports(item, _ip_address)
                _ports_list.append(_ports)

                _organization = self.retrieve_org(item)
                _organization_list.append(_organization)

                _city = self.retrieve_city(item)
                _city_list.append(_city)

                _location = self.retrieve_country_code(item)
                _location_list.append(_location)

                _postal_code = self.retrieve_postal_code(item)
                _postal_code_list.append(_postal_code)

                _longitude, _latitude = self.retrieve_longitude_latitude(item)
                _longitude_list.append(_longitude)
                _latitude_list.append(_latitude)

                _data, _server = self.retrieve_data(item)
                _data_list.append(_data)
                _server_list.append(_server)

                _cve = self.retieve_cve(_ip_address)
                _cve_list.append(_cve)

                print('\n')
                sleep(1)

                device_instance = DeviceInstance(device_id=index, server_os=_server, organization=_organization,
                                                 transport=_transport, ip_address=_ip_address, ports=_ports,
                                                 data_layer=_data, location=_location, city=_city,
                                                 postal_code=_postal_code, longitude=_longitude, latitude=_latitude,
                                                 cve=_cve)

                self.report_engine.write_device_report(device_instance)

            pandas_engine = PandasEngine()
            pandas_engine.create_dataframe(_server_list, _organization_list, _transport_list, _ip_address_list,
                                           _ports_list, _data_list, _location_list, _city_list, _postal_code,
                                           _longitude_list, _latitude_list, _cve_list)
            return _filtered_data
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))

    def retrieve_transport(self, item):
        '''

        :param item:
        :return:
        '''

        try:
            _transport = item['transport']
            if _transport is not None:
                self.logger.info('{0} Transport Retrieved: {1}'.format(self.name,  _transport.upper()))
                return _transport.upper()
            return 'None'
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return ' - '

    def retrieve_ip_address(self, item):
        '''

        :param item:
        :return:
        '''
        try:
            _ip_address = item['ip_str']
            if _ip_address is not None:
                self.logger.info('{0} Ip Address Retrieved: {1}'.format(self.name,  _ip_address))
                return _ip_address
            return 'None'
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return ' - '

    def retrieve_ports(self, item, ip_address):
        '''

        :param item:
        :param ip_address:
        :return:
        '''
        try:
            _port = item['port']
            if _port is not None:
                try:
                    _ports = self.shodan_api.host(ip_address, True)['ports']
                    self.logger.info('{0} Ports Retrieved: {1}'.format(self.name, _ports))
                    return _ports
                except Exception as err:
                    print(err)
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return ' - '

    def retrieve_org(self, item):
        '''

        :param item:
        :return:
        '''
        try:
            _organization = item['org']
            if _organization is not None:
                self.logger.info('{0} Organization Retrieved: {1}'.format(self.name, _organization))
                return _organization
            return 'None'
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return ' - '

    def retrieve_city(self, item):
        '''

        :param item:
        :return:
        '''
        try:
            _city = item['location']['city']
            if _city is not None:
                self.logger.info('{0} City Retrieved: {1}'.format(self.name, _city.title()))
                return _city.title()
            return 'None'
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return ' - '

    def retrieve_country_code(self, item):
        '''

        :param item:
        :return:
        '''
        try:
            _country_code3 = item['location']['country_code3']
            if item['location']['country_code3'] is not None:
                self.logger.info('{0} Country Code3 Retrieved: {1}'.format(self.name, _country_code3.upper()))
                return _country_code3.upper()
            return 'None'
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return ' - '

    def retrieve_postal_code(self, item):
        '''

        :param item:
        :return:
        '''
        try:
            _postal_code = item['location']['postal_code']
            if _postal_code is not None:
                self.logger.info('{0} Postal Code Retrieved: {1}'.format(self.name, _postal_code))
                return _postal_code
            return 'None'
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return ' - '

    def retrieve_longitude_latitude(self, item):
        '''

        :param item:
        :return:
        '''
        try:
            _longitude = item['location']['longitude']
            _latitude = item['location']['latitude']
            if (_longitude and _latitude) is not None:
                self.logger.info('{0} Longitude, Latitude Retrieved: {1}, {2}'.format(self.name, _longitude, _latitude))
                return _longitude, _latitude
            return 'None', 'None'
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return ' - ', ' - '

    def retrieve_data(self, item):
        '''

        :param item:
        :return:
        '''
        try:
            _data = item['data']
            if _data is not None:
                _data = re.search('HTTP/(1.[0-9]?)', item['data'], re.IGNORECASE).group(0)
                _server = re.search('Server: .*', item['data'], re.IGNORECASE).group(0)[len('Server: '):-1]
                self.logger.info('{0} Data, Server OS Retrieved: {1}, {2}'.format(self.name, _data, _server))
                return _data, _server
            return 'None', 'None'
        except AttributeError as err:
            self.logger.error('{0} CVE Retrieved: {1}'.format(self.name, err))
            return 'None', 'None'
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return ' - ', ' - '

    def retieve_cve(self, ip_address):
        '''

        :param ip_address:
        :return:
        '''
        try:
            _aux_result = self.shodan_api.host(ip_address, True)
            if _aux_result.get('vulns') is not None:
                _cve = _aux_result.get('vulns')
                self.logger.info('{0} CVE Retrieved: {1}'.format(self.name, _cve ))
                return _cve

            self.logger.info('{0} CVE Retrieved: {1}'.format(self.name, ''))
            return []
        except Exception as err:
            self.logger.fatal('{0} CVE Retrieved: {1}'.format(self.name, err))
            return []
