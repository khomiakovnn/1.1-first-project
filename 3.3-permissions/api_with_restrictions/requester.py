import requests


def make_adv(token, title, description):
    href = 'http://127.0.0.1:8000/api/advertisements/'
    headers = {
        'authorization': 'Token ' + token,
    }
    params = {
        'title': title,
        'description': description
    }
    response = requests.post(href, headers=headers, data=params)
    print(response.text)
    print(response.status_code)


def show_adv(adv_id):
    href = 'http://127.0.0.1:8000/api/advertisements/' + str(adv_id) + '/'
    response = requests.get(href)
    print(response.text)
    print(response.status_code)


def del_adv(token, adv_id):
    href = 'http://127.0.0.1:8000/api/advertisements/' + str(adv_id) + '/'
    headers = {
        'authorization': 'Token ' + token,
    }

    response = requests.delete(href, headers=headers)
    print(response.text)
    print(response.status_code)

def update_adv(token, adv_id, title, description, status):
    href = 'http://127.0.0.1:8000/api/advertisements/' + str(adv_id) + '/'
    headers = {
        'authorization': 'Token ' + token,
    }
    data = {
        'title': title,
        'description': description,
        'status': status
    }
    response = requests.patch(href, data=data, headers=headers)
    print(response.text)
    print(response.status_code)


if __name__ == '__main__':
    token_admin = 'a0a1eef5ee878028643618adfd096981829bb333'
    token_user1 = '9c2caac175b0c0aeec3956bf3bf2aad0fedc6033'
    token_user2 = '81171a1ba4da71a02d8b81f69fd05976cbc5d4f4'

    # Функции работы с объявлениями
    # make_adv(token_user1, 'XXXX', 'WWWWW')  # Создать объявление
    # show_adv(15)  # Показать объявление
    # del_adv(token_admin, 12)  # Удалить объявление
    # update_adv(token_admin, 11, 'Меняем', 'Админ', 'CLOSED')  # Изменить объявление
