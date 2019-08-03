from django.contrib import admin
from AdminDashboard.models import AdminProfile,WorkAssign,AdminPost,AdminReminder

# Register your models here.
admin.site.register(AdminProfile)
admin.site.register(WorkAssign)
admin.site.register(AdminPost)
admin.site.register(AdminReminder)