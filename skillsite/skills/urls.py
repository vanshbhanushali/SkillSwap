from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),            # redirects root to login
    path('login/', views.fake_login, name='login'),         # login view
    path('register/', views.register, name='register'),     # optional register
    path('home/', views.home, name='home'),                 # home page
    path('myswaps/', views.my_swaps, name='my_swaps'),      # my swaps page
    path('profile/', views.profile, name='profile'),        # profile page
    path('browse/', views.browse, name='browse'),           # ✅ this fixes your error
    path('messages/', views.messages, name='messages'),

]
