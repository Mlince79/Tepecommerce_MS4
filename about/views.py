from django.shortcuts import render

def about(request):
    """ A view to see about the illustrator """

    return render(request, 'about/about.html')
