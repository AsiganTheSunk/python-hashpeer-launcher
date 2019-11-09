#!/usr/bin/env python


# Import Geo & Country Database Modules
from countryinfo import CountryInfo
import geopy.distance
import pycountry


# Import System Modules
import csv


class CountryInstance:
    def __init__(self, country_name='Unknown'):
        self.name = self.__class__.__name__
        self.country_name, self.country_alpha_2, self.country_alpha_3 = self._get_country_names(country_name)

        if country_name != 'Unknown':
            try:
                self.country_official_name = pycountry.countries.get(name=self.country_name).official_name
            except:
                self.country_official_name = 'Unknown'
                #print('UKNOWN COUNTRY')
        else:
            self.country_official_name = 'Unknown'
        self.country_borders = self._get_country_borders(self.country_name, self.country_official_name)
        self.country_latitude, self.country_longitude = self._get_centroid(self.country_name, self.country_official_name)

    @staticmethod
    def _get_country_names(country_name):
        """
            This Function,

        :param country_name:
        :return:
        """
        try:
            if len(country_name) == 2:
                return pycountry.countries.get(alpha2=country_name).name, \
                       country_name, \
                       pycountry.countries.get(alpha_2=country_name).alpha_3

            if len(country_name) == 3:
                return pycountry.countries.get(alpha_3=country_name).name, \
                       pycountry.countries.get(alpha_3=country_name).alpha_2, \
                       country_name

            return country_name, \
                   pycountry.countries.get(name=country_name).alpha_2, \
                   pycountry.countries.get(name=country_name).alpha_3

        except Exception as err:
            return '__', '___', 'Unknown'

    @staticmethod
    def _get_country_borders(country_name, country_official_name):
        """
            This Function,

        :param country_name:
        :param country_official_name:
        :return:
        """

        if country_name != 'Unknown':
            try:
                return CountryInfo(country_name).info()['borders']
            except KeyError as err:
                try:
                    return CountryInfo(country_official_name).info()['borders']
                except KeyError as err:
                    return ['0', '0']
        return ['0', '0']

    @staticmethod
    def _get_country_border_coordinates(country_name, country_official_name):
        '''
            This Function,
        :param country_name:
        :param country_official_name:
        :return:
        '''
        if country_name != 'Unknown':
            try:
                return CountryInfo(country_name).info()['geoJSON']['features'][0]['geometry']['coordinates'][0]
            except Exception as err:
                return CountryInfo(country_official_name).info()['geoJSON']['features'][0]['geometry']['coordinates'][0]
        return []

    @staticmethod
    def _get_centroid(country_name, country_official_name):
        '''
            This Function
        :param country_name:
        :param country_official_name:
        :return:
        '''
        if country_name != 'Unknown':
            with open('./curlstem/geo_data/country_centroids.csv', mode='r', encoding='ISO-8859-1') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                result = {}
                line_count = 0
                for row in csv_reader:
                    result[row['name'].lower()] = [row['latitude'], row['longitude']]
                    line_count += 1
            try:
                return result[country_name.lower()][0], result[country_name.lower()][1]
            except:
                return result[country_official_name.lower()][0], result[country_official_name.lower()][1]
        return '0', '0'

    @staticmethod
    def _get_country_centroid(country_borders_coordinates):
        '''
            This Function, will calculate the centroid of a country given it's border coordinates.Taking into account
        that with coordinates that close to each other, you can treat the Earth as being locally flat to retrieve the
        centroid as though they were planar coordinates. Then the function will take the average of the latitudes and
        the average of the longitudes to find the latitude and longitude of the centroid.

        :param country_borders_coordinates:
        :return: country_latitude_centroid, country_longitude_centroid
        '''
        latitude = []
        longitude = []
        try:
            if any(isinstance(i, list) for i in country_borders_coordinates[0]):
                country_borders_coordinates = country_borders_coordinates[0]
                for coordinates in country_borders_coordinates:
                    longitude.append(coordinates[0])
                    latitude.append(coordinates[1])
                return sum(longitude)/len(longitude), sum(latitude)/len(latitude)

            for coordinates in country_borders_coordinates:
                longitude.append(coordinates[0])
                latitude.append(coordinates[1])
            return sum(longitude) / len(longitude), sum(latitude) / len(latitude)

        except:
            return 0, 0

    def get_distance_from_country(self, latitude, longitude):
        """
            This Function, will calculate the distance from the CountryIntance to the coordinates you provide. Because
        when using Haversine formula, we assume, the earth it's spherical, this will get errors of 0.5%. To solve this,
        we implemented the function using Vincenty distance, just because it uses more precise elipsoidal models
        like WGS-84.

        :param longitude:
        :param latitude:
        :return: Distance in (km) from the source Instance Country.
        """

        country_centroid_distance = geopy.distance.vincenty((self.country_latitude, self.country_longitude),
                                                            (latitude, longitude)).km
        return country_centroid_distance

