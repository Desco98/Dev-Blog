from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('contacts/', include('contacts.urls')),
    path('posts/', include('posts.urls')),
]
