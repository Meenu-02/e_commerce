from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect


from ec_app.forms import LoginRegister, SellerRegister, CustomerRegister, SellerForm
from ec_app.models import Customer, Seller, Product_Add


# Create your views here.

def home(request):
    return  render(request,'home.html')

def dashboard(request):
    return render(request,'index.html')

# def login_page(request):
#     return render(request,'login.html')

def seller_add(request):
    form1= LoginRegister()
    form2= SellerRegister()


    if request.method == 'POST':
        form3 = LoginRegister(request.POST)
        form4= SellerRegister(request.POST)



        if form3.is_valid() and form4.is_valid():
            a = form3.save(commit=False)
            a.is_seller = True
            a.save()


            user1 = form4.save(commit=False)
            user1.user = a
            user1.save()

            return redirect('login_view')


    return render(request,'seller_registration.html',{'form1':form1,'form2':form2})


def customer_add(request):
    form1=LoginRegister()
    form2=CustomerRegister()

    if request.method == 'POST':
        form3= LoginRegister(request.POST)
        form4= CustomerRegister(request.POST)
        if form3.is_valid() and form4.is_valid():
            a= form3.save(commit=False)
            a.is_customer = True
            a.save()
            user1 = form4.save(commit=False)
            user1.user = a
            user1.save()

            return redirect('login_view')
    return render(request,'customer_registration.html',{'form1':form1,'form2':form2})

def cus_reg(request):
    return  render(request,'cus_reg.html')


def customer_base(request):
    return render(request,'customer/customer.html')

def seller_base(request):
    return render(request,'seller/seller.html')

def admin_base(request):
    return render(request,'admin/admin.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')

        password = request.POST.get('pass')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin')  #url name
            elif user.is_customer:
                return redirect('cus_prod')
            elif user.is_seller:
                return redirect('seller')

        else:
            messages.info(request,'Invalid Credentials')

    return render(request,'login.html')


def view_customer(request):
    data= Customer.objects.all()
    return render(request,'admin/customer_view.html',{'view_customer':data})

def view_seller(request):
    data= Seller.objects.all()
    return render(request,'admin/seller_view.html',{'view_seller':data})


def delete_customer(request,id):
    data=Customer.objects.get(id=id)

    data.delete()
    return redirect('customer_view')  #give url(name) for redirect

def delete_seller(request,id):
    data=Seller.objects.get(id=id)
    data.delete()
    return redirect('seller_view')


def update_customer(request,id):
    data=Customer.objects.get(id=id)
    form=CustomerRegister(instance=data) #form will be with data


    if request.method =='POST':
         details = CustomerRegister(request.POST,instance=data)
         if details.is_valid():
             details.save()
             return  redirect('customer_view')
    return render(request,'admin/customer_update.html',{'update':form})

def update_seller(request,id):
    data=Seller.objects.get(id=id)
    form=SellerRegister(instance=data) #form will be with data


    if request.method =='POST':
         details = SellerRegister(request.POST,instance=data)
         if details.is_valid():
             details.save()
             return  redirect('seller_view')
    return render(request,'admin/seller_update.html',{'update':form})


def seller_form_upload(request):

    data=request.user
    seller_data=Seller.objects.get(user=data)




    if request.method == 'POST':
        form = SellerForm(request.POST, request.FILES)

        if form.is_valid():
            object = form.save(commit=False)
            object.user = seller_data
            object.save()

            return redirect('home')
    else:
        form = SellerForm()
    return render(request, 'seller/seller_form.html', {
        'form': form
    })

# def seller_product(request):
#     data= Product_Add.objects.all()
#
#     return render(request,'seller/seller_product.html',{'seller_product':data})

#
# def products_admin(request):
#     data=Product_Add.objects.all()
#     return render(request,'admin/products.html',{'products':data })

# def products_customer(request):
#     data=Product_Add.objects.all()
#     return render(request,'customer/products.html',{'product':data})