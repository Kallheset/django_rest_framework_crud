from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = 'id', 'title', 'description', 'technologies', 'created_at' # estos son los campos que estan en la base de datos
        read_only_fields = ('created_at',)# se coloca asi porq es una campo de solo lectura