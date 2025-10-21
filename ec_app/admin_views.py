from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ec_app.filters import SellerFilter, DisplayFilter
from ec_app.models import Product_Add, Buy

@login_required(login_url='login_view')
def products_admin(request):
    data=Product_Add.objects.all()
    sellerFilter = SellerFilter(request.GET, queryset=data)
    s = sellerFilter.qs
    context = {
        'products': s,
        'sellerFilter': sellerFilter
    }
    return render(request,'admin/products.html',context)


@login_required(login_url='login_view')
def display(request):
    data=Buy.objects.all()
    displayFilter = DisplayFilter(request.GET, queryset=data)
    s = displayFilter.qs
    context = {
        'object': s,
        'displayFilter': displayFilter
    }
    return render(request,'admin/display.html',context)
