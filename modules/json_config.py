import json


def save_in_json(dictionary, file_dir):
    """Принимает на вход словарь (dictionary) значений и сохраняет в файл JSON"""
    with open(file_dir, 'w') as file:
        json.dump(dictionary, file)


def load_json(name):
    """Функция загрузки JSON в переменную"""
    try:
        with open(name, 'r') as file_user:
            file = json.load(file_user)
            print(f"{name} - loading successful")
            return file
    except FileNotFoundError:
        # Если файл не найден, начинаем с пустого словаря
        file = {}
        print(f"{name} not found, we make a new :)")
        return file
