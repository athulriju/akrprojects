from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from shop.models import Category, Product

# Create your views here.
# def home(req):
#     return HttpResponse('jvhbjh')

def allprod(req, c_slug=None):
    c_page = None
    products_list = None
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list, 3)
    try:
        page = int(req.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
        
    return render(req, 'category.html', {'category': c_page, 'products': products})

def prod_deets(req, c_slug, p_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(req, 'products.html', {'product': product})
