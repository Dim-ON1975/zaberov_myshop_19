import json
import os

from core.settings import BASE_DIR


def json_save(name: str, phone: str, message: str) -> None:
    """
    Запись данных формы в json-файл.
    :param name: Имя, str.
    :param phone: Телефон, str.
    :param message: Сообщение, str.
    """
    data = {'name': str(name), 'phone': str(phone), 'message': str(message)}
    path = os.path.join(BASE_DIR, 'catalog', 'messages', 'messages.json')
    with open(path, 'r', encoding='utf8') as file:
        data_json = json.load(file)
        data_json['messages'].append(data)
        with open(path, 'w', encoding='utf8') as outfile:
            json.dump(data_json, outfile, ensure_ascii=False, indent=2)


