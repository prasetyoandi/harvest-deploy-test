from django.urls import path
from .views import Spk

urlpatterns = [
    path('', Spk.as_view(), name='spk'),
    path('<int:project_id>/', Spk.as_view(), name='spk_project'),
]
