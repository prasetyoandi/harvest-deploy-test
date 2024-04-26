"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from calculate.views import Calculate

urlpatterns = [
    path('', include('users.urls')),
    path('boards/', include('task_manager.urls')),
    path('report/', include('reports.urls')),
    path('spk/', include('spk.urls')),
    path('calculate/', include('calculate.urls')),
    path('admin/', admin.site.urls),
    path('calculate', Calculate.as_view(), name='calculate')

]

# handler404 = 'djangoProject.errorViews.handler404'
# handler500 = 'djangoProject.errorViews.handler500'
