"""geekshop URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', mainapp.main, name='main'),
    path('contact/', mainapp.contact, name='contact'),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/',  include('authapp.urls', namespace='auth')),
    path('basket/',  include('basketapp.urls', namespace='basket')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
