from django.contrib import admin
from UserManagement.models import *

admin.site.register(CustomUser)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(BlogModel)
# Register your models here.
