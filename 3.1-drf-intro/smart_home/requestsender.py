import random

import requests

# ----- Добавление датчика
# href = 'http://127.0.0.1:8000/api/sensors/'
# param = {
#   "name": "ESP32",
#   "description": "Датчик на кухне за холодильником"
# }
# response = requests.post(href, data=param)
# print(response.text)

# ----- Изменение датчика
# href = 'http://127.0.0.1:8000/api/sensors/1/'
# param = {
#     "name": "Новое наименование датчика",
#     "description": "Перенес датчик на балкон",
# }
# response = requests.patch(href, data=param)
# print(response.text)


# ----- Измерение температуры
href = 'http://127.0.0.1:8000/api/measurements/'
param = {
    "sensor": random.choice([1, 2, 3]),
    "temperature": random.uniform(17.5, 35.5)
    "image": "image"
}
response = requests.post(href, data=param)
print(response.text)
