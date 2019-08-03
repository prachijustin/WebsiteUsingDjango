from django.conf.urls import url
from front import views
# from AdminDashboard import views as v

app_name = 'front'

urlpatterns = [
                # url(r'^$', v.index_post_list,name='index_post_list'),
                url(r'^$', views.index,name='index'),
               
                url(r'new1/$',views.new1,name='new1'),
                url(r'new2/$',views.new2,name='new2'),
                url(r'new3/$',views.new3,name='new3'),
                url(r'new4/$',views.new4,name='new4'),
                url(r'new5/$',views.new5,name='new5'),
                url(r'new7/$',views.new7,name='new7'),
                url(r'new8/$',views.new8,name='new8'),
                url(r'new9/$',views.new9,name='new9'),
                url(r'new10/$',views.new10,name='new10'),
                url(r'about/$',views.about,name='about'),
                url(r'(?P<id>\d+)/post_detail/$',views.post_detail,name='post_detail'),
                url(r'feedback/$',views.feedback,name='feedback'),
               ]