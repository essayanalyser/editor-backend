from rest_framework import serializers
from .models import EditorUsers,HistoryData

class EditorUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditorUsers
        fields = ('title','version','content')

class HistoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryData
        # data = serializers.JSONField()
        fields = ('key','data')