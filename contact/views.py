from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'contact/email.html', {'form': form})