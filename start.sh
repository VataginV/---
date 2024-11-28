#!/bin/bash

# Активируем виртуальное окружение
source /home/tos6591766/xn---75-redpe9d.ru/docs/my_venv/bin/activate

# Переходим в директорию проекта
cd /home/tos6591766/xn---75-redpe9d.ru/docs/SiteTOS

# Запускаем сервер Django на указанном IP и порту
python manage.py runserver 0:8174