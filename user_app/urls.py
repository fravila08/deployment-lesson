from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_capabilities, name='user_capabilities'),
    # path('', views.send_the_index, name='index')
]
