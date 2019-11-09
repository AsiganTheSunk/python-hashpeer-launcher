#!/usr/bin/python3

#
import pandas as pd
from pandas import DataFrame

pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 1400)


class PandasEngine():
    def __init__(self):
        self.name = self.__class__.__name__

    def create_dataframe(self, _server_list, _organization_list, _transport_list, _ip_address_list, _ports_list,
                         _data_layer_list, _location_list, _city_list, _postal_code_list, _longitude_list,
                         _latitude_list, _cve_list):

        raw_data = {'device_os': _server_list,
                    'organization': _organization_list,
                    'transport': ['TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP', 'TCP'],
                    'address': _ip_address_list,
                    'ports': _ports_list,
                    'data': _data_layer_list,
                    'location': _location_list,
                    'city': _city_list,
                    'postal_code': _postal_code_list,
                    'longitude': _longitude_list,
                    'latitude': _latitude_list,
                    'cve': _cve_list}

        dataframe = DataFrame(raw_data)
        print(dataframe)
        return DataFrame(raw_data)
