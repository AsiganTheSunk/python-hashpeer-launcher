#!/usr/bin/env python


class Response(str):
    def __new__(cls, code, _type, data):
        return str.__new__(cls, data)

    def __init__(self, code, _type, data):
        self.code = code
        self.type = _type
        self.data = data
        str.__init__(self)


