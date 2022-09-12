from django.contrib import admin

from nurse import models

admin.site.register(models.Nurse)
admin.site.register(models.Visitor)
admin.site.register(models.Row)
