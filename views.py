from django.shortcuts import render

# Create your views here.
def pagenotfound(request):

    return render(request,'main/404.html')

def blog_single(request):

    return render(request,'main/blog-single.html')

def blog(request):

    return render(request,'main/blog.html')

def cart(request):

    return render(request,'main/cart.html')


def checkout(request):

    return render(request,'main/checkout.html')

def contact_us(request):

    return render(request,'main/contact-us.html')

def index(request):

    return render(request,'main/index.html')

def login(request):

    return render(request,'main/login.html')

def product_details(request):

    return render(request,'main/product-details.html')

def shop(request):

    return render(request,'main/shop.html')