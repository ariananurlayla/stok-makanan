from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    items = Item.objects.all()
    jumlah_item = len(items)
    context = {
        'name': 'Ariana Nurlayla Syabandini',
        'class': 'PBP C',
        'items': items,
        'jumlah_item': jumlah_item,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)