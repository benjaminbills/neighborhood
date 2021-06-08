from django.urls import path
from . import views


urlpatterns = [
  path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
  path('logout/', views.logoutUser, name="logout"),
  path('', views.home, name='home' ),
  path('user/<int:user_id>', views.userPage, name='user_page'),
  path('account/', views.accountSettings, name='account'),
  path('add_business/', views.addBusiness, name='add_business'),
  path('get_businesses/', views.getBusinesses, name='get_businesses'),
]
