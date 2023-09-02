from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # Add paths for login, logout, etc.
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('personal-info/', views.personal_info, name='personal_info'),
    path('etm-info/', views.etm_info, name='etm_info'),
    path('schedule/', views.schedule_view, name='schedule'),


]

