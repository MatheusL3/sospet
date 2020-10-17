from django.shortcuts import render


def places(request):
    template_name = 'places/places.html'
    return render(request, template_name)
