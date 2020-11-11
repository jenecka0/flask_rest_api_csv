import csv

from .support import get_data_file_path


def read_all_users_from_csv_file(app):
    with open(get_data_file_path(app), 'r') as read_file:
        reader = csv.DictReader(read_file, delimiter=';')
        data_read = [row for row in reader]

    return data_read


def write_new_user_to_csv_file(app, data_to_write):
    with open(get_data_file_path(app), 'a', newline='') as write_file:
        fieldnames = ['id', 'name', 'last_name', 'description', 'employee']
        writer = csv.DictWriter(
            write_file,
            delimiter=';',
            fieldnames=fieldnames
        )
        write_new_line_to_csv_file(app)
        writer.writerow(data_to_write)


def write_new_line_to_csv_file(app):
    with open(get_data_file_path(app), 'a', newline='') as write_file:
        write_file.write("\n")


def generate_id_to_new_user(app):
    users = read_all_users_from_csv_file(app)
    users = sorted(users, key=lambda k: int(k['id']))
    id_number = int(users[-1]['id']) + 1

    return id_number


def delete_row_from_csv_file(app, user_id):
    with open(get_data_file_path(app), 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        data_to_write = []
        for row in reader:
            if row['id'] == str(user_id):
                continue

            data_to_write.append(row)

    field_names = data_to_write[0].keys() if data_to_write else []
    with open(get_data_file_path(app), 'w', newline='') as write_file:
        writer = csv.DictWriter(
            write_file,
            delimiter=';',
            fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data_to_write)


def modify_row_to_csv_file(app, user_id, new_user_data):
    with open(get_data_file_path(app), 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        data_to_write = []
        for row in reader:
            if row['id'] == str(user_id):
                data_to_write.append(new_user_data)
                continue

            data_to_write.append(row)

    field_names = data_to_write[0].keys() if data_to_write else []
    with open(get_data_file_path(app), 'w', newline='') as write_file:
        writer = csv.DictWriter(
            write_file,
            delimiter=';',
            fieldnames=field_names
        )
        writer.writeheader()
        writer.writerows(data_to_write)


def search_user_from_csv_file(app, user_id):
    users = read_all_users_from_csv_file(app)
    for data in users:
        if data['id'] == str(user_id):
            return data

    return None
