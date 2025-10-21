from tkinter.font import names

from django.urls import path

from ec_app import views, admin_views, seller_views, customer_views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    # path('login_page',views.login_page,name='login_page'),
    path('seller_add',views.seller_add,name='seller_add'),
    path('customer_add',views.customer_add,name='customer_add'),
    #path('cus_reg',views.cus_reg,name='cus_reg'),
    path('customer',views.customer_base,name='customer'),
    path('seller',views.seller_base,name='seller'),
    path('admin',views.admin_base,name='admin'),
    path('login_view',views.login_view,name='login_view'),
    path('customer_view',views.view_customer,name='customer_view'),
    path('seller_view',views.view_seller,name='seller_view'),
#delete
    path('delete_customer/<int:id>/',views.delete_customer,name='delete_customer'),
  path('delete_seller/<int:id>/',views.delete_seller,name='delete_seller'),
    #update
    path('update_customer/<int:id>/',views.update_customer,name='update_customer'),
path('update_seller/<int:id>/',views.update_seller,name='update_seller'),
    path('seller_form',views.seller_form_upload,name='seller_form'),

    #seller
    path('seller_product',seller_views.seller_product,name='seller_product'),
    path('sell_prod_up/<int:id>/',seller_views.update_product,name='sell_prod_up'),
    path('sell_prod_del/<int:id>/',seller_views.delete_product,name='sell_prod_del'),
    path('sell_profile',seller_views.profile,name='sell_profile'),
    path('sell_prof_up/<int:id>',seller_views.update_profile,name='sell_prof_up'),
    path('orderlist',seller_views.order_seller,name='orderlist'),


    #admin
    path('products',admin_views.products_admin,name='products'),
    path('display',admin_views.display,name='display'),


    #customer
    path('cus_prod',customer_views.products_customer,name='cus_prod'),
path('description/<int:pk>/', customer_views.description, name='description'),
    path('profile',customer_views.profile,name='profile'),
    path('prof_up/<int:id>/',customer_views.profile_update,name='prof_up'),
    path('cart/<int:id>',customer_views.cart_item,name='cart'),
    path('cartitem',customer_views.cart_view,name='cartitem'),
    path('cartremove/<int:id>/',customer_views.cart_remove,name='cartremove'),
    path('buy/<int:id>/',customer_views.buy_product,name='buy'),
    path('order',customer_views.order_list,name='order'),
    path('cartbuy/<int:id>/',customer_views.cart_buy,name='cartbuy'),


#logout
    path('logout_view',views.logout_view,name='logout_view')




]