from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('plants/', views.PlantList.as_view(), name='plant_list'),
    path('plants/<int:pk>', views.PlantDetail.as_view(), name='plant_detail'),
    path('blogs/', views.BlogList.as_view(), name="blog_list"),
    path('blogs/<int:pk>', views.BlogDetail.as_view(), name="blog_detail"),
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/<int:pk>', views.UserDetail.as_view(), name="user_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
