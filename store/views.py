from django.shortcuts import render


def categories_view(request):
    return render(request, 'categories.html')

