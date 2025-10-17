from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from ec_app.filters import ProductFilter
from ec_app.forms import CustomerRegister, BuyForm
from ec_app.models import Product_Add, Customer, Cart, Buy


def products_customer(request):
    data=Product_Add.objects.all()
    productFilter = ProductFilter(request.GET,queryset=data)
    s = productFilter.qs
    context = {
        'product': s,
        'productFilter':productFilter
    }
    return render(request,'customer/products.html',context)



def description(request, pk):
    product = Product_Add.objects.get(pk=pk)
    #product = get_object_or_404(Product_Add, pk=pk)
    return render(request, 'customer/description.html', {'product': product})

def profile(request):
    cus = request.user
    data=Customer.objects.get(user=cus)
    return render(request,'customer/profile.html',{'profile': data})

def profile_update(request,id):
    data=Customer.objects.get(id=id)
    form=CustomerRegister(instance=data)

    if request.method == 'POST':
        details = CustomerRegister(request.POST,instance=data)
        if details.is_valid():
            details.save()
            return redirect('profile')


    return render(request,'customer/profile_update.html',{'update':form})

def cart_item(request,id):
    cus=request.user
    products= Product_Add.objects.all()
    data=Customer.objects.get(user=cus)

    prod=Product_Add.objects.get(id=id)

    filter_data=Cart.objects.filter(user=data,product=prod)

    if filter_data.exists():
        messages.info(request,'Product Already Added To Cart')

    else:
        item = Cart()
        item.user = data
        item.product = prod
        item.save()

        return redirect('cus_prod')


    return render(request,'customer/products.html',{'product':products})

def cart_view(request):
    cus= request.user
    person=Customer.objects.get(user=cus)#only a data is stored
    data=Cart.objects.filter(user=person)  #a list of data is stored
    return render(request,'customer/cart.html',{'cart':data})

def cart_remove(request,id):
    data=Cart.objects.get(id=id)
    data.delete()
    return redirect('cartitem')

def buy_product(request,id):
    data=request.user
    customer_data = Customer.objects.get(user=data)
    products = Product_Add.objects.get(id=id)
    details=BuyForm()
    available_qty=products.quantity


    if request.method == 'POST':
        details = BuyForm(request.POST)

        if details.is_valid():
            given_count = details.cleaned_data.get('count')
            if  given_count <= available_qty:


               object = details.save(commit=False)
               object.user = customer_data

               object.product = products
               object.save()
               total_qty = available_qty - given_count
               products.quantity = total_qty
               products.save()
               return redirect('cus_prod')

            else:
                messages.info(request,'Out of Stock')


    return render(request,'customer/buyproduct.html',{'form':details})


def order_list(request):
    cus = request.user
    person = Customer.objects.get(user=cus)

    data=Buy.objects.filter(user=person)
    return render(request,'customer/order_list.html',{'order':data})

def cart_buy(request,id):
    data = Cart.objects.get(id=id)
    customer = data.user
    products = data.product
    details = BuyForm()
    available_item = products.quantity

    if request.method == 'POST':
        details = BuyForm(request.POST)

        if details.is_valid():
            given_count = details.cleaned_data.get('count')
            if given_count <= available_item:

                object=details.save(commit=False)
                object.user= customer
                object.product=products
                object.save()
                total_item = available_item - given_count
                products.quantity=total_item
                products.save()
                return redirect('cus_prod')

            else:
                messages.info(request,'Out of Stock')


    return render(request,'customer/buyproduct.html',{'form':details})

def order_seller(request):

