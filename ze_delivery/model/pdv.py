from mongoframes import *
from .geometry_type import GeometryType

class Pdv(Frame):

    _fields = {
        'id',
        'tradingName',
        'ownerName',
        'document',
        'coverageArea',
        'address'
    }


class CoverageArea(GeometryType):

    _fields = {
        'type',
        'coordinates'
    }


class Address(GeometryType):

    _fields = {
        'type',
        'coordinates'
    }