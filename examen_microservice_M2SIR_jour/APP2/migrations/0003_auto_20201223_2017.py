# Generated by Django 3.1.4 on 2020-12-23 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP2', '0002_auto_20201223_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusetudiant',
            name='montant',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='statusetudiant',
            name='statut',
            field=models.CharField(max_length=30),
        ),
    ]
