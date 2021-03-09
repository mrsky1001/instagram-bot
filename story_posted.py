import os

from csv_worker import csv_reader, csv_write_line, csv_clear

file_name = 'story_posted.csv'


def get_story_posted():
    if not os.path.isfile(file_name):
        open(file_name, 'a').close()

    with open(file_name, "r") as f_obj:
        list_lines = csv_reader(f_obj)

    return list_lines


def clear_story():
    csv_clear(file_name)


def add_story(name):
    csv_write_line(name, file_name)
