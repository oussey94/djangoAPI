from rest_framework import serializers
from .models import StatusEtudiant

class StatusEtudiantSerializer(serializers.ModelSerializer):
     class Meta:
        model = StatusEtudiant
        fields = '__all__'