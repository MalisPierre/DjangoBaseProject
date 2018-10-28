from django.shortcuts import render, redirect
from django import template
from common.forms import TroubleshoutingForm
from emailing.views_common import send_troubleshouting

from django.http import HttpResponseRedirect

def home(request):    
    return render(request, 'common/home.html', {})

def maintenance(request):
    return render(request, 'common/maintenance.html')

def troubleshouting(request):
    if request.method == 'POST':
        form = TroubleshoutingForm(request.POST)
        if form.is_valid():
            cool = form.cleaned_data['cool']
            comment = form.cleaned_data['comment']
            if cool == "oui":
                send_troubleshouting(True, comment)
            else:
                send_troubleshouting(False, comment)
            return redirect (troubleshouting_sended)
        else:
            return render(request, 'common/troubleshouting.html', {'form': form, })
    else:
        form = TroubleshoutingForm()
        return render(request, 'common/troubleshouting.html', {'form': form, })

def troubleshouting_sended(request):
    return render(request, 'common/troubleshouting_sended.html')
