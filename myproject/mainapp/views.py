from .models import *
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
def shopPage(request):
    shoes = Shoes.objects.all()
    context = {
        "shoes": shoes
    }
    return render(request, "mainapp/index.html", context)

def mycontact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'ВЫ успешно прошли регистрацию')
            return redirect('homepage')
        else:
            messages.info(request, 'ОШИБКА')

    context = {
            'form': form
        }

    return render(request, 'form_app/index.html', context)