import os

#who is the SMTP server impersonnating


#SMTP CONFIG - GMAIL
EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.sendgrid.net'

EMAIL_HOST_USER = 'XXX'

EMAIL_HOST_PASSWORD = 'XXXX'

EMAIL_PORT = 587
