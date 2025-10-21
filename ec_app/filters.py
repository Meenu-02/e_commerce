import django_filters
from django import forms
from django_filters import CharFilter


from ec_app.models import Product_Add, Buy


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'Search',
                                                                                     'class':'nav-link mt-2 mt-md-0 d-none d-lg-flex search'}))

    class Meta:
        model = Product_Add
        fields = ('name',)


class SellerFilter(django_filters.FilterSet):
    user__name = CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'Search',
                                                                                     'class':'nav-link mt-2 mt-md-0 d-none d-lg-flex search'}))


    class Meta:
        model = Product_Add
        fields = ('user__name',)


class SellerproductFilter(django_filters.FilterSet):
    name = CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'Search',
                                                                                     'class':'nav-link mt-2 mt-md-0 d-none d-lg-flex search'}))

    class Meta:
        model = Product_Add
        fields = ('name',)



class DisplayFilter(django_filters.FilterSet):
    product__user__name = CharFilter(label="",lookup_expr='icontains',widget=forms.TextInput(attrs={'placeholder':'Search',
                                                                                     'class':'nav-link mt-2 mt-md-0 d-none d-lg-flex search'}))

    class Meta:
        model = Buy
        fields = ('product__user__name',)