# Generated by Django 3.1.4 on 2020-12-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP2', '0003_auto_20201223_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusetudiant',
            name='montant',
            field=models.IntegerField(default=0),
        ),
    ]
