from django.conf.urls import url
from AdminDashboard import views


#set the NAMESPACE
app_name='AdminDashboard'

urlpatterns = [
       url(r'test/$',views.test,name='test'),
       url(r'dashboard/$',views.dashboard,name='dashboard'),
       url(r'add_reminder/$',views.add_reminder,name='add_reminder'),
       url(r'login/$',views.user_login,name='user_login'),
       url(r'reg/$',views.reg,name='reg'),
       url(r'create/$',views.post_create,name='add_post'),
       url(r'(?P<id>\d+)/$',views.post_detail,name='detail'),
       url(r'^posts/',views.post_list,name='all_posts'),
       url(r'(?P<id>\d+)/edit/$',views.post_update,name='update'),
       url(r'(?P<id>\d+)/delete/$',views.post_delete,name="delete"),
       url(r'(?P<id>\d+)/emp_edit/$',views.emp_edit,name='emp_edit'),
       url(r'(?P<id>\d+)/emp_delete/$',views.emp_delete,name="emp_delete"),
       url(r'allposts/$',views.all_posts_list,name='allp'),
       url(r'all_employees/$',views.all_employees,name='all_employees'),
       url(r'assign_work/$',views.assign_work,name='assign_work'),
       url(r'(?P<id>\d+)/work_detail/$',views.work_detail,name='work_detail'),
       url(r'(?P<id>\d+)/track_emp_reason/$',views.track_emp_reason,name='track_emp_reason'),
       url(r'add_employee/$',views.add_employee,name='add_employee'),
       url(r'track_emp_detail/$',views.track_emp_detail,name='track_emp_detail'),
       url(r'track_emp_list/$',views.track_emp_list,name='track_emp_list'),
       url(r'feedback/$',views.feedback,name='feedback'),
       url(r'(?P<id>\d+)/feedback_delete/$',views.feedback_delete,name="feedback_delete"),
       url(r'(?P<id>\d+)/feedback_detail/$',views.feedback_detail,name='feedback_detail'),
]