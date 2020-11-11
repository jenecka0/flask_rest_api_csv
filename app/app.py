from flask import Flask, abort, jsonify

from .support.data_manipulation import delete_row_from_csv_file, generate_id_to_new_user, modify_row_to_csv_file, \
    read_all_users_from_csv_file, search_user_from_csv_file, write_new_user_to_csv_file
from .support.request_handling import read_user_attributes_from_request
from .support.support import setup_app


DEFAULT_DATA_FILE_PATH = './data/users.csv'
API_PREFIX = '/api/v1'

app = Flask(__name__)

setup_app(app, DEFAULT_DATA_FILE_PATH)


@app.route('/', methods=['GET'])
def health():

    return "OK", 200


@app.route(API_PREFIX + '/users', methods=['GET'])
def get_user():
    users = read_all_users_from_csv_file(app)

    return jsonify(users)


@app.route(API_PREFIX + '/users/<user_id>', methods=['GET'])
def get_ids(user_id):
    if not user_id.isdigit():
        return abort(400)

    data = search_user_from_csv_file(app, user_id)
    if not data:
        return abort(404)

    return jsonify(data)


@app.route(API_PREFIX + '/users', methods=['POST'])
def add_user():
    user = read_user_attributes_from_request()
    user['id'] = generate_id_to_new_user(app)
    write_new_user_to_csv_file(app, user)

    return jsonify(user)


@app.route(API_PREFIX + '/users/<user_id>', methods=['DELETE'])
def remove_user(user_id):
    if not user_id.isdigit():
        return abort(400)

    deleted_user = search_user_from_csv_file(app, user_id)
    if not deleted_user:
        return abort(400)

    delete_row_from_csv_file(app, user_id)

    return jsonify(deleted_user)


@app.route(API_PREFIX + '/users/<user_id>', methods=['PUT'])
def modify_user(user_id):
    if not user_id.isdigit():
        return abort(400)

    new_user_data = read_user_attributes_from_request()
    if not new_user_data:
        abort(400)

    user_to_be_modified = search_user_from_csv_file(app, user_id)
    if not user_to_be_modified:
        return abort(404)

    user_to_be_modified['name'] = new_user_data['name']
    user_to_be_modified['last_name'] = new_user_data['last_name']
    user_to_be_modified['description'] = new_user_data['description']
    user_to_be_modified['employee'] = new_user_data['employee']

    modify_row_to_csv_file(app, user_id, user_to_be_modified)
    user_after_modify = search_user_from_csv_file(app, user_id)

    return jsonify(user_after_modify)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
