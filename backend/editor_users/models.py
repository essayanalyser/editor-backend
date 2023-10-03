from django.db import models

# Create your models here.
class EditorUsers(models.Model):
    title = models.CharField(max_length=100,primary_key=True)
    version = models.IntegerField()
    content = models.TextField()
    
    def _str_(self):
        return self.title