from rest_framework import serializers
from .models import EditorUsers

class EditorUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorUsers
        fields = ('title','version','content')

