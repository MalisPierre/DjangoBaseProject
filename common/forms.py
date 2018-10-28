from django import forms

PART_CHOICES = (
        ('oui', 'oui'),
        ('non', 'non'),)

class TroubleshoutingForm(forms.Form):
    cool = forms.ChoiceField(choices = PART_CHOICES,required = True, label="Telechargeriez vous l'application")
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 3, 'rows': 20}), required=False, label="commentaires")
