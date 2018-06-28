from flask import jsonify
from mongoframes import *
from pdv_challenge.model.pdv import Pdv, Validation


class Controller(object):

    @staticmethod
    def json_response(message, code):
        return jsonify({'message': message}), code


class PdvController(Controller):

    @staticmethod
    def frame_json_response(frame):
        if isinstance(frame, Frame):
            return jsonify(frame.to_json_type())

        return PdvController.json_response('Error', 500)

    @staticmethod
    def _build_mongo_geo_query(lat, lng, operator):
        return {
            'coverageArea': {
                operator: {
                    '$geometry': {
                        'type':
                            "Point",
                            'coordinates': [lng, lat]
                    }
                }
            }
        }


    @staticmethod
    def get_intersects_or_near_pdv(lat, lng):
        if lat is None or lng is None:
            return PdvController.json_response('Not found', 404)

        #PDV inside polygon
        pdv = Pdv.one(
            PdvController._build_mongo_geo_query(lat, lng, '$geoIntersects')
        )

        # Pdv near from polygon
        if pdv is None:
            pdv = Pdv.one(
                PdvController._build_mongo_geo_query(lat, lng, '$near')
            )

        return PdvController.frame_json_response(pdv)

    @staticmethod
    def get_pdv_by_id(id):
        pdv = Pdv.one(Q.id == id, projection={'_id': False})
        if pdv is None:
            return PdvController.json_response('Not found', 404)

        return PdvController.frame_json_response(pdv)

    @staticmethod
    def create_pdv(payload):
        status, message = Validation.validate(payload)
        if not status:
            return PdvController.json_response(message, 400)
        try:
            Pdv(payload).insert()
            return PdvController.json_response('created', 201)
        except Exception as e:
            return PdvController.json_response(str(e), 400)
