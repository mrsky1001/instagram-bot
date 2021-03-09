import csv


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    list_lines = []

    for row in reader:
        list_lines.append(row)
    return list_lines


def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    list_lines = []

    for line in reader:
        list_lines.append(line["name"])
        list_lines.append(line["date"])

    return list_lines


def csv_clear(path):
    f = open(path, "w+")
    f.close()


def csv_write_line(data, path):
    with open(path, "a+", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([data])
