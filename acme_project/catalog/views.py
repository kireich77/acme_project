from django.shortcuts import render

#Класс HttpResponse нужно импортировать в код из модуля django.http.
from django.http import HttpResponse

def product_list(request):
    template_name = 'catalog/product_list.html'
    title = 'Список товаров ACME'
    products = [
      'Iron carrot',
      'Giant mousetrap',  
      'Dehydrated boulders',
      'Invisible paint',
    ]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, template_name, context) 

def product_detail(request):    
    template_name = 'catalog/product_detail.html'
    return render(request, template_name) 

def product_category(request, category):    
    return HttpResponse(f'Категория {category}')