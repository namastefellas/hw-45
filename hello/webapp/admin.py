from django.contrib import admin
from webapp.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title', 'status']
    fields = ['id', 'title', 'status']
    readonly_fields = ['id']


admin.site.register(Task, TaskAdmin)