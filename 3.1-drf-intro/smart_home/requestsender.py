import random

import requests

# ----- Проверка метода POST
# href = 'http://127.0.0.1:8000/api/sensors/'
# param = {
#   "name": "ESP32",
#   "description": "Датчик на кухне за холодильником"
# }
# response = requests.post(href, data=param)
# print(response.text)

# ----- Проверка метода PATH
# href = 'http://127.0.0.1:8000/api/sensors/1/'
# param = {
#     "name": "Новое наименование датчика",
#     "description": "Перенес датчик на балкон",
# }
# response = requests.patch(href, data=param)
# print(response.text)


# ----- Проверка создания измерения
# href = 'http://127.0.0.1:8000/api/measurements/'
# param = {
#     "sensor": random.choice([1, 2, 3]),
#     "temperature": random.uniform(17.5, 35.5)
# }
# response = requests.post(href, data=param)
# print(response.text)
