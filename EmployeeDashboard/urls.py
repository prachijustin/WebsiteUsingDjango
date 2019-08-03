from django.conf.urls import url
from . import views as v

#set the NAMESPACE
app_name='EmployeeDashboard'

urlpatterns = [
       url(r'emp_auth/$',v.emp_auth,name='emp_auth'),
       url(r'employee_dashboard/$',v.employee_dashboard,name='employee_dashboard'),
       url(r'add_reminder/$',v.add_reminder,name='add_reminder'),
       url(r'emp_assign_work/$',v.emp_assign_work,name='emp_assign_work'),
       url(r'report_work/$',v.report_work,name='report_work'),
       url(r'(?P<id>\d+)/emp_work_detail/$',v.emp_work_detail,name='emp_work_detail'),

       ]