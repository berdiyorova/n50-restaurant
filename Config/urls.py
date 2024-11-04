from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls', namespace='users')),
    path('', include('app_menu.urls', namespace='menu')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
