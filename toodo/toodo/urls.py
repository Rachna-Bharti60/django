
from django.contrib import admin
from django.urls import path, include
from toodo_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('toodo_list.urls')),
]
