# urls.py
from django.urls import path
from .views import create_profile,resume,list

urlpatterns = [
    path('', create_profile, name='create_profile'),
    path('<int:id>/',resume, name='resume'),
    path('list/',list, name='list')
]
