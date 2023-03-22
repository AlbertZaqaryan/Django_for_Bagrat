from django.shortcuts import render, redirect
from .models import (SiteName, HomeBg, 
                     Info, Product, 
                     AboutClient, Client, 
                     Contact)
from .forms import ContactForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(**form.cleaned_data)
            return redirect('index')
    else:
        form = ContactForm()
    site_name = SiteName.objects.all()[0]
    home_bg = HomeBg.objects.all()[0]
    info_list = Info.objects.all()
    product_list = Product.objects.all()
    about_client = AboutClient.objects.all()[0]
    client_list = Client.objects.all()
    return render(request, 'main/index.html', context={
        'site_name':site_name,
        'home_bg':home_bg,
        'info_list':info_list,
        'product_list':product_list,
        'about_client':about_client,
        'client_list':client_list,
        'form':form
    })