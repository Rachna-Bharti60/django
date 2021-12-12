
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('',views.home,name="home"),
    path('delete/<List_id>',views.delete,name ="delete"),
    path('cross_off/<List_id>',views.cross_off,name ="cross_off"),
    path('uncross/<List_id>',views.uncross,name ="uncross"),
    path('edit/<List_id>',views.edit,name ="edit"),
]
