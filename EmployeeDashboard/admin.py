from django.contrib import admin
from EmployeeDashboard.models import EmployeeProfile,ReportWork,EmployeeReminder

# Register your models here.
admin.site.register(EmployeeProfile)
admin.site.register(ReportWork)
admin.site.register(EmployeeReminder)