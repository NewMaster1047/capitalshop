from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')


def categories_view(request):
    return render(request, 'categories.html')


def login_view(request):
    return render(request, 'login.html')


def cart_view(request):
    return render(request, 'cart.html')


def pro_details_view(request):
    return render(request, 'pro-details.html')


def checkout_view(request):

    return render(request, 'checkout.html')


def blog_view(request):
    return render(request, 'blog.html')


def blog_details_view(request):
    return render(request, 'blog-details.html')


def blog_details_view_(request):
    return render(request, 'blog_details.html')


def elements_view(request):
    return render(request, 'elements.html')


def contact_view(request):
    return render(request, 'contact.html')


