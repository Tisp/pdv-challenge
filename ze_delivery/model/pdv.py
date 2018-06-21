from mongoframes import *
from .geometry_type import GeometryType
from jsonschema import validate, ValidationError


class Pdv(Frame):

    _fields = {
        'id',
        'tradingName',
        'ownerName',
        'document',
        'coverageArea',
        'address'
    }

    _private_fields = {
        '_id'
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


class Validation(object):
    _schema = {
        "type": "object",
        "$schema": "http://json-schema.org/draft-06/schema#",
        "properties": {
            "id": {
                "type": "string"
            },
            "tradingName": {
                "type": "string"
            },
            "ownerName": {
                "type": "string"
            },
            "document": {
                "type": "string"
            },
            "coverageArea": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "coordinates": {
                        "type": "array",
                        "items": {
                            "type": "array",
                            "items": {
                                "type": "array",
                                "items": {
                                    "type": "array",
                                    "items": {
                                        "type": "number"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "address": {
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string"
                    },
                    "coordinates": {
                        "type": "array",
                        "items": {
                            "type": "number"
                        }
                    }
                }
            }
        },
        "required": ["id", "tradingName", "ownerName", "document", "coverageArea", "address"]
    }

    @staticmethod
    def validate(pdv):
        try:
            validate(pdv, Validation._schema)
            return True, None
        except ValidationError as e:
            return False, str(e).split("\n")[0]

