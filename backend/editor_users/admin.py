from django.contrib import admin
from .models import EditorUsers,HistoryData
# Register your models here.

class EditorUsersAdmin(admin.ModelAdmin):
    list = ("title","content")
    
admin.site.register(EditorUsers,EditorUsersAdmin)
admin.site.register(HistoryData,EditorUsersAdmin)