from django.urls import path
from .views import Spk

urlpatterns = [
    path('', Spk.as_view()),

]
