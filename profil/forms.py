from django import forms

class UserConnectionForm(forms.Form):
    pseudo = forms.CharField(label='Nom du compte')
    password = forms.CharField(widget=forms.PasswordInput())

class UserSubscriptionForm(forms.Form):
    pseudo = forms.CharField(label='Nom du compte')
    email = forms.EmailField(label='adresse email')
    password = forms.CharField(widget=forms.PasswordInput(),label='Mot de passe')
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label='Retapez votre mot de passe')
  
class ChangeEmailForm(forms.Form):
    new_email = forms.EmailField()
    
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

class ChangePhotoForm(forms.Form):
    photo = forms.ImageField(label='Image de profil')
