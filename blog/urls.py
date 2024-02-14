from django.urls import path
from .views import (home_view, categories_view,
                    login_view, cart_view,
                    pro_details_view, checkout_view,
                    blog_view, elements_view,
                    blog_details_view, blog_details_view_,
                    contact_view
                    )

urlpatterns = [
    path('', home_view),
    path('categories/', categories_view),
    path('login/', login_view),
    path('cart/', cart_view),
    path('pro_detals/', pro_details_view),
    path('checkout/', checkout_view),
    path('blog/', blog_view),
    path('blog_details/', blog_details_view),  # blog-details.html
    path('blog_details_/', blog_details_view_),  # blog_details.html
    path('elements/', elements_view),
    path('contact/', contact_view),

]


