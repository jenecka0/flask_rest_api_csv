from app.app import API_PREFIX, app

import webtest

from .shared import setup_app_for_test


def test_users_list_returns_code_200():
    my_app = webtest.TestApp(app)
    setup_app_for_test(app)

    resp = my_app.get(API_PREFIX + '/users')
    assert resp.status_int == 200
    assert resp.json


def test_users_list_returns_non_empty_list_of_users():
    my_app = webtest.TestApp(app)
    setup_app_for_test(app)

    resp = my_app.get(API_PREFIX + '/users')
    assert resp.status_int == 200
    assert resp.json
    assert isinstance(resp.json, list)

    users_list = resp.json
    assert users_list


def test_user_in_db_with_id_returns_code_200():
    my_app = webtest.TestApp(app)
    setup_app_for_test(app)

    resp = my_app.get(API_PREFIX + '/users/1')
    assert resp.status_int == 200
    assert resp.json


def test_adds_user_to_db_and_returns_code_200():
    my_app = webtest.TestApp(app)
    setup_app_for_test(app)

    new_user_data = {
        "name": "USER_NAME",
        "last_name": "LAST_NAME",
        "description": "POSITION"
    }
    resp = my_app.post_json(API_PREFIX + '/users', new_user_data)
    new_user_id = resp.json["id"]
    actual_result = my_app.get(API_PREFIX + '/users/{}'.format(new_user_id))

    assert actual_result.status_int == 200
    assert resp.status_int == 200
    assert actual_result.json
    assert new_user_data["name"] == actual_result.json["name"]
    assert new_user_data["last_name"] == actual_result.json["last_name"]
    assert new_user_data["description"] == actual_result.json["description"]


def test_delete_user_from_db_returns_code_200():
    my_app = webtest.TestApp(app)
    setup_app_for_test(app)

    resp = my_app.delete_json(API_PREFIX + '/users/1')

    assert resp.status_int == 200
    assert resp.json


def test_edit_user_to_db_and_returns_code_200():
    my_app = webtest.TestApp(app)
    setup_app_for_test(app)

    new_user_data = {
        "name": "USER_NAME",
        "last_name": "LAST_NAME",
        "description": "POSITION"
    }
    resp = my_app.put_json(API_PREFIX + '/users/1', new_user_data)
    actual_result = my_app.get(API_PREFIX + '/users/1')

    assert resp.status_int == 200
    assert actual_result.status_int == 200
    assert new_user_data["name"] == actual_result.json["name"]
    assert new_user_data["last_name"] == actual_result.json["last_name"]
    assert new_user_data["description"] == actual_result.json["description"]
