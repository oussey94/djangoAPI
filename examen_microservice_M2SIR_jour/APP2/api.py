from rest_framework import viewsets
from .serializers import StatusEtudiantSerializer
from .models import StatusEtudiant

class StatusEtudiantViewSet(viewsets.ModelViewSet):
	serializer_class = StatusEtudiantSerializer
	queryset = StatusEtudiant.objects.all()