from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('auth/', include('authentication.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


