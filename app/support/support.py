DATA_FILE_PATH_CONFIG_ACCESS_KEY = 'DATA_FILE_PATH'


def get_data_file_path(app):
    return app.config[DATA_FILE_PATH_CONFIG_ACCESS_KEY]


def setup_app(app, data_file_path):
    app.config[DATA_FILE_PATH_CONFIG_ACCESS_KEY] = data_file_path
