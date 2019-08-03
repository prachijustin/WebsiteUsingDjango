from django.conf.urls import url
from Search_Company import views

app_name='Search_Company'

urlpatterns = [
    url(r'^$',views.search_company,name='search_company'),
    url(r'^search$', views.search, name='search'),
    url(r'^company$', views.fetch_company_data, name='company'),
]