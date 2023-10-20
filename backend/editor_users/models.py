from django.db import models

# Create your models here.
class EditorUsers(models.Model):
    title = models.CharField(max_length=100,primary_key=True)
    version = models.CharField(max_length=2)
    content = models.TextField()
    # data_json = models.JSONField()
    
    def _str_(self):
        return self.title

class HistoryData(models.Model):
    key = models.ForeignKey(EditorUsers,on_delete=models.CASCADE) 
    # doc_id = models.BigIntegerField()
    doc_name = models.CharField(max_length=100)
    data = models.JSONField() 