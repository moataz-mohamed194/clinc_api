from django.contrib import admin

from doctor import models

admin.site.register(models.Fees)
admin.site.register(models.Doctor)
admin.site.register(models.Clinic)
