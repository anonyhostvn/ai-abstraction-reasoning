import json
import os


class InputMachine:

    def __init__(self):
        return

    @staticmethod
    def read_test_input(dir_name):
        list_input = []
        for file_name in os.listdir(dir_name):
            path = os.path.join(dir_name, file_name)
            with open(path) as file_data:
                data = json.load(file_data)
                list_input.append(data)

        return list_input
