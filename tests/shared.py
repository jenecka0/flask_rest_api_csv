import os
import shutil
import uuid

from app.support.support import setup_app

TEST_DATA_FILE_PATH = './tests/data/users.csv'
TMP_FILE_PATH = './tmp'


def setup_app_for_test(app):
    assert os.path.exists(TEST_DATA_FILE_PATH)

    if not os.path.exists(TMP_FILE_PATH):
        os.mkdir(TMP_FILE_PATH)

    test_data_file_name = str(uuid.uuid4())

    test_file_name = os.path.join(TMP_FILE_PATH, test_data_file_name)
    shutil.copy(TEST_DATA_FILE_PATH, test_file_name)

    setup_app(app, test_file_name)
