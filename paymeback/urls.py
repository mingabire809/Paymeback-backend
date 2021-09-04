"""paymeback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='paymeback')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_lender/',include('my_lender.urls')),
    path('my_borrower/',include('my_borrower.urls')), 
    path('account/',include('account.urls')),
    path('transaction/',include('transaction.urls')),
    path('',schema_view),
    path('accounts/',include('rest_framework.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)