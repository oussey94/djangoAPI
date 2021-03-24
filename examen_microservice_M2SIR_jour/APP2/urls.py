from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .api import StatusEtudiantViewSet

router=DefaultRouter()
router.register(r'statutEtudiant', StatusEtudiantViewSet, basename="statutEtudiant")

urlpatterns = [
    path("api/", include(router.urls)),
]
