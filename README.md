# DjangoBaseProject
Django Project 

Thi project is set up to work on a local machine and on a heroku environment
See the website in action here: https://djangoayomi.herokuapp.com/common/home

To Launch the project on a localmachine :

1) Have python and pip installed -> python environment (workon MyPythonEnv) is advised
2) pip install -r requirements.txt
3) edit the file config/settings.py -> set the var [DEPLOYMENT_MODE = 'Heroku'] to [DEPLOYMENT_MODE = 'Local']
4) python manage.py makemigrations
5) python manage.py migrate
6) python manage.py init_database
7) python manage.py runserver

