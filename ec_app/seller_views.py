from django.shortcuts import render, redirect

from ec_app.filters import SellerproductFilter
from ec_app.forms import SellerForm, SellerRegister
from ec_app.models import Product_Add, Seller


def seller_product(request):
    data= Product_Add.objects.all()
    sellerproductFilter = SellerproductFilter(request.GET, queryset=data)
    s = sellerproductFilter.qs
    context = {
        'seller_product': s,
        'sellerproductFilter': sellerproductFilter
    }

    return render(request,'seller/seller_product.html',context)

def update_product(request,id):
    data=Product_Add.objects.get(id=id)
    form = SellerForm(instance=data)

    if request.method == 'POST':
        details = SellerForm(request.POST,request.FILES,instance=data)
        if details.is_valid():
            details.save()
            return redirect('seller_product')

    return render(request,'seller/seller_product_update.html',{'update':form})


def delete_product(request,id):
    data=Product_Add.objects.get(id=id)
    data.delete()
    return redirect('seller_product')

def profile(request):
    data = request.user
    seller = Seller.objects.get(user=data)
    return render(request,'seller/profile.html',{'profile':seller})

def update_profile(request,id):
    data = Seller.objects.get(id=id)
    form = SellerRegister(instance=data)

    if request.method == 'POST':
        details = SellerRegister(request.POST,instance=data)
        if details.is_valid():
            details.save()
            return redirect('sell_profile')

    return render(request,'seller/profile_update.html',{'update':form})