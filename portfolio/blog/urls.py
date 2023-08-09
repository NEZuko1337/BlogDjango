from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


app_name = "elem"

urlpatterns = [
    path('', views.all_blogs, name = "all_blogs"),
    path('<int:pk>/', views.details, name = "detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


