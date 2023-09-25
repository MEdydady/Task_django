#!/bin/bash
cd /home/medy/Task_django/3.2-crud/stocks_products
git pull origin video
source env/bin/activate
python manage.py migrate
deactivate
sudo systemctl restart gunicorn  
