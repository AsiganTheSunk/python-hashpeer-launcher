#!/usr/bin/python3


class CVEInstance():
    def __init__(self, cve):
        self.name = self.__class__.__name__
        self.cve = cve
        self._properties = {}

    def __getitem__(self, key):
        if key == 'properties':
            return self._properties
        return self._properties[key]

    def __str__(self):
        return
