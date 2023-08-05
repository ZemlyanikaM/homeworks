"""
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа. При перезапуске функции уже записанные в файл данные должны сохраняться.
"""
__all__ = ['create_users']

import json
import os

ACCESS_LEVELS = [1, 2, 3, 4, 5, 6, 7]


def create_users(json_path: str) -> None:
    users_id = set()
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as df:
            data = json.load(df)
            for user in data.values():
                users_id.update(user.keys())
    else:
        data = {str(access_level): dict() for access_level in range(1, 8)}

    while True:
        name: str = input('Enter name: ')
        if not name:
            break
        user_id = input('Enter ID: ')
        access_level = input("Enter access level: ")
        if user_id in users_id:
            continue
        data[access_level][user_id] = name
        with open(json_path, 'w', encoding='utf-8') as df:
            json.dump(data, df, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    create_users('users.json')
