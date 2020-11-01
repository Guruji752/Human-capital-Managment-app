#!/bin/bash
cp /opt/project_files/hcm/production.py /home/aditshsoft/development/hcm_management/aditshsoft/aditshsoft/settings/
cd /home/aditshsoft
source dev/bin/activate
cd /home/aditshsoft/development/hcm_management/aditshsoft
sudo kill -9 $(sudo lsof -t -i:8001)
python3 manage.py migrate
nohup python3 manage.py runserver 0:8001 >/dev/null 2>&1 &
