#!/usr/bin/python3

default = ' - '


class DeviceInstance():
    def __init__(self, device_id=default, server_os=default, organization=default, transport=default,
                 ip_address=default, ports=default, data_layer=default, location=default, city=default,
                 postal_code=default,  longitude=default, latitude=default, cve=default):

        self.name = self.__class__.__name__

        # Device Information
        self.device_id = str(device_id)
        self.server_os = str(server_os)
        self.organization = str(organization)

        # Network Information
        self.transport = transport
        self.ip_address = ip_address
        self.ports = ports
        self.data_layer = str(data_layer)

        # Country Information
        self.location = str(location)
        self.city = str(city)
        self.postal_code = str(postal_code)
        self.longitude = str(longitude)
        self.latitude = str(latitude)

        # CVE Vulnerabilities
        self.cve = cve
        self._properties = {'device_id': self.device_id,
                            'device_os': self.server_os,
                            'organization': self.organization,
                            'transport_layer': {'protocol': self.transport},
                            'network_layer': {'ip_address': self.ip_address, 'ports': self.ports},
                            'data_layer': {'protocol': self.data_layer},
                            'geo_data': {'location': self.location, 'city': self.city,
                                         'postal_code': self.postal_code,
                                         'longitude': self.longitude, 'latitude': self.latitude}
                            }

    def __getitem__(self, key):
        if key == 'properties':
            return self._properties
        return self._properties[key]

    def __str__(self):
        return '\nDevice Number: {0} \n' \
               'Organization: {1}\n' \
               'Brand:\n' \
               'Device OS: {2}\n' \
               'Data Layer: {3}\n' \
               'Transport Layer: {4}\n' \
               'Network Layer: {5}:{6}\n' \
               'Location: {7} \n' \
               'City: {8}\n' \
               'Postal Code: {9} \n' \
               'Coordinates: ( {10}, {11} )\n' \
               'Datasheet:\n' \
               'Shodan Url: https://www.shodan.io/host/{12}\n' \
               ''.format(self['device_id'],
                         self['organization'],
                         self['device_os'],
                         self['data_layer']['protocol'],
                         self['transport_layer']['protocol'],
                         self['network_layer']['ip_address'], self['network_layer']['ports'],
                         self['geo_data']['location'],
                         self['geo_data']['city'],
                         self['geo_data']['postal_code'],
                         self['geo_data']['longitude'], self['geo_data']['latitude'],
                         self['network_layer']['ip_address'])
