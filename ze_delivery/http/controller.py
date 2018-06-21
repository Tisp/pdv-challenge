from flask import jsonify
from mongoframes import *
from ze_delivery.model.pdv import Pdv, Validation


class Controller(object):

    @staticmethod
    def json_response(message, code):
        return jsonify({'message': message}), code


class PdvController(Controller):

    @staticmethod
    def frame_json_response(frame):
        if isinstance(frame, Frame):
            return jsonify(frame.to_json_type())

        return False

    @staticmethod
    def get_near_pdv(lat, lng):
        if lat is None or lng is None:
            return PdvController.json_response('Not found', 404)

        pdv = Pdv.one({
            'coverageArea': {
                '$near': {
                    '$geometry': {
                        'type':
                            "Point",
                            'coordinates': [lng, lat]
                    }
                }
            }
        })

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

        Pdv(payload).insert()
        return PdvController.json_response('created', 201)





