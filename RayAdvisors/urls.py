"""RayAdvisors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from AdminDashboard import views
from front import views as f
from EmployeeDashboard import views as v

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', f.index,name='index'),
    url(r'^site_admin/',include('AdminDashboard.urls')),
    url(r'^employee/',include('EmployeeDashboard.urls')),
    url(r'^SearchCompany/',include('Search_Company.urls',namespace='Search_Company')),
    url(r'^front/',include('front.urls')),
    url(r'^special/',views.special,name='special'),
    url(r'^$',views.user_logout,name='logout'),
    url(r'^special/',v.special,name='special'),
    url(r'^$',v.user_logout,name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)