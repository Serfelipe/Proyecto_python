from django.shortcuts import render

from . import models

def home(request):
    query = models.Comision.objects.all()
    context = {'App':query}
    return render(request, 'App/index.html', context)


from django.shortcuts import render