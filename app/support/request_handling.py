from flask import abort, request


def read_user_attributes_from_request():
    if not request.json:
        abort(400)

    required_fields = ['name', 'last_name', 'description']
    for required_field in required_fields:
        if required_field not in request.json:
            print("Missd field: '{}'".format(required_field))
            abort(400)

    user = {
        'name': request.json['name'],
        'last_name': request.json['last_name'],
        'description': request.json['description'],
        'employee': bool(request.json.get('employee', False))
    }

    return user
