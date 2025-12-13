from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # Custom profile views (Oscar handles auth)
    path('', views.profile, name='profile'),
    path('edit/', views.profile_edit, name='profile_edit'),
]
