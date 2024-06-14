from django.shortcuts import render

from . import models

def home(request):
    query = models.Comision.objects.all()
    context = {'clientes':query}
    return render(request, 'cliente/index.html', context)


from django.shortcuts import render