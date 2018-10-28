from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.conf import settings

def get_html(text):
    footer = "<p>Cordialement,</p><p>l e quipe " + settings.WEBSITE_NAME_STR + " </p><p>tout droit reserver</p>"
    return text + footer

def send_email(from_email, to_email, subject_email, text_content, html_content):
    email = EmailMultiAlternatives(subject_email, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()
    return True
