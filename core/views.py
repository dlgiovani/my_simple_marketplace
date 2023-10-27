from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from core.models import contactParm


def index(request):
    items_ = Item.objects.filter(is_sold=False).order_by('?')[:9]

    items = [items_[i:i+3] for i in range(0, len(items_), 3)]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    whatsapp = contactParm.objects.first()
    whatsapp_number = whatsapp.product_contact_whatsapp_phone
    whatsapp_link = f'https://api.whatsapp.com/send?phone={whatsapp.product_contact_whatsapp_phone}&text=Olá, vim pelo site do Rei do Saco Preto :)'

    return render(request, 'core/contact.html', {
        'whatsapp_link': whatsapp_link,
        'whatsapp_number': whatsapp_number
    })

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:

        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })