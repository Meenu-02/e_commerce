from django.shortcuts import render

from ec_app.filters import SellerFilter
from ec_app.models import Product_Add



def products_admin(request):
    data=Product_Add.objects.all()
    sellerFilter = SellerFilter(request.GET, queryset=data)
    s = sellerFilter.qs
    context = {
        'products': s,
        'sellerFilter': sellerFilter
    }
    return render(request,'admin/products.html',context)