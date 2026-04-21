from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_role, name='select'),
    path('home/', views.home, name='home'),

    path('donor-login/', views.donor_login, name='donor_login'),
    path('donor-register/', views.donor_register, name='donor_register'),

    path('org-login/', views.org_login, name='org_login'),
    path('org-register/', views.org_register, name='org_register'),

    path('donate/', views.donate, name='donate'),
    path('request/', views.request_page, name='request'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_view, name='logout'),
]