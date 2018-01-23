def read_data_file(file_path):
    elements = []

    with open(file_path, 'r') as db:
        elements.extend(line.strip() for line in db.readlines())

    return elements
