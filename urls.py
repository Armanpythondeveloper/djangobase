from django.urls import path

from .import views

urlpatterns = [

    path('',views.index,name = 'index'),
    path('404/',views.pagenotfound,name = '404'),
    path('blog-single/',views.blog_single,name = 'blog-single'),
    path('blog/',views.blog,name = 'blog'),
    path('cart/',views.cart,name = 'cart'),
    path('checkout/',views.checkout,name = 'checkout'),
    path('contact-us/',views.contact_us,name = 'contact-us'),
    path('login/',views.login,name = 'login'),
    path('product-details/',views.product_details,name = 'product-details'),
    path('shop',views.shop,name = 'shop')

]