from django.urls import path
from .views import Calculate

urlpatterns = [
    path('', Calculate.as_view(), name='calculate')
]
