# DjangoBaseProject
Django Project 

Thi project is set up to work on a local machine and on a heroku environment
See the website in action here: https://djangoayomi.herokuapp.com/common/home

To Launch the project on a localmachine :

1) Have python and pip installed -> python environment (workon MyPythonEnv) is advised

2) pip install -r requirements.txt

3) edit the file config/settings.py
set the var [DEPLOYMENT_MODE = 'Heroku'] to [DEPLOYMENT_MODE = 'Local']

4) edit the file config/settings/local_settings/email_settings and setup the variables to a valid SMTP server
set [EMAIL_HOST_USER = 'XXXX@gmail.com'] to your gmail address
set [EMAIL_HOST_PASSWORD = 'XXXX'] to your gmail password
Make sure your gmail allow to SMTP https://support.google.com/a/answer/6260879

5) python manage.py makemigrations

6) python manage.py migrate

7) python manage.py init_database

8) python manage.py runserver

9) you're good to go !

