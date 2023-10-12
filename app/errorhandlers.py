from flask import jsonify


def not_found(error):
    return jsonify(success=False, error=404, message="Not Found"), 404


def bad_request(error):
    return jsonify(success=False, error=400, message="Bad Request"), 400


def method_not_allowed(error):
    return jsonify(success=False, error=405, message="Method Not Allowed"), 405
