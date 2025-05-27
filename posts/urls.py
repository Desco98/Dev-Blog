from django.urls import path
from . import views

urlpatterns = [
    path('latest', views.lpost, name = 'latest'),
    path('<int:post_id>', views.post, name = 'post'),
]