# Generated by Django 3.1.1 on 2020-09-06 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminhospital', '0002_remove_turno_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turno',
            old_name='hour',
            new_name='date_hour',
        ),
    ]
