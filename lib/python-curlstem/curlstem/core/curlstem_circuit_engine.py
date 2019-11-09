import geoip2.database

# System Modules
import socket

class CircuitEngine:
    def __init__(self):
        self.name = self.__class__.__name__

    def get_hostname_ip(self, hostname):
        # TODO: esto lo deberia buscar a traves de una conexion auxiliar de TOR, en
        # TODO: la que da igual la velocidad, o hacerlo en claro, aunque no se yo
        ip_hostname = socket.gethostbyname(hostname)
        print('Hostname Ip Address: {0}'.format(ip_hostname))
        return ip_hostname

    def get_hostname_location(self, ip_hostname):
        reader = geoip2.database.Reader('./curlstem/geo_data/GeoLite2-City.mmdb')
        ip_location = reader.city(ip_hostname)
        #print('Location Ip Address: {0}'.format(ip_location.country.name))
        return ip_location.country.name


