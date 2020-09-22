from django.shortcuts import render

# Create your views here.

def about(request):
    """ A view to see about the illustrator """

    return render(request, 'about/about.html')
