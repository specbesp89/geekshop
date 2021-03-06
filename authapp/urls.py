from django.urls import path

import authapp.views as authapp_views

app_name = 'authapp'

urlpatterns = [
   path('login/', authapp_views.login, name='login'),
   path('register/', authapp_views.UserRegisterView.as_view(), name='register'),
   path('logout/', authapp_views.logout, name='logout'),
   path('profile/', authapp_views.profile, name='profile'),

]
