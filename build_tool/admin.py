from django.contrib import admin

from .models import Project, Asset, Step, BuildSession

# Register your models here.

admin.site.register(Project)
admin.site.register(Asset)
admin.site.register(Step)
admin.site.register(BuildSession)