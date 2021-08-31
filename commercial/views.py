from django.shortcuts import render
from . import models

# Create your views here.


def homepage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phonenumber")
        relation = request.POST.get("relation")
        information = request.POST.get("message")
        new_counsel = models.Counseling.objects.create(
            name=name, phone_number=phone_number, relation=relation, information=information)
        return render(request, 'commercial/home.html', {"modal": True})
    return render(request, 'commercial/home.html')
