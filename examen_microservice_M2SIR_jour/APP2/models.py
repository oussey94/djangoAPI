from django.db import models

# Create your models here.

class StatusEtudiant(models.Model):
	nom=models.CharField(max_length=30)
	prenom=models.CharField(max_length=30)
	statut=models.CharField(max_length=30)
	montant=models.IntegerField(default=0)