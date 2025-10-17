from cProfile import label

from django.contrib.auth.forms import UserCreationForm
from django import forms

from ec_app.models import Customer, Seller, Login, Product_Add, Buy


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(label='password', widget = forms.PasswordInput)
    password2 =  forms.CharField(label='confirm password', widget= forms.PasswordInput)
    class Meta:
        model = Login
        fields = ('username','password1','password2',)


class CustomerRegister(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('user',)

class SellerRegister(forms.ModelForm):
    class Meta:
        model = Seller
        fields = '__all__'
        exclude = ('user',)


class SellerForm(forms.ModelForm):
    class Meta:
        model = Product_Add
        fields = ('name','description','picture','quantity','price',)


class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = '__all__'
        exclude = ('status','user','product',)