from django.contrib import admin
from .models import EditorUsers
# Register your models here.

class EditorUsersAdmin(admin.ModelAdmin):
    list = ("title","content")
    
admin.site.register(EditorUsers,EditorUsersAdmin)