from django.shortcuts import render

def contactEmail(request):
    """ A view that renders the contact details of the illustrator """

    return render(request, 'contactemail/contactemail.html')
