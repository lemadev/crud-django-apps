# Generated by Django 3.1.1 on 2020-09-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminhospital', '0006_auto_20200907_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='observations',
            field=models.TextField(blank=True, null=True),
        ),
    ]
