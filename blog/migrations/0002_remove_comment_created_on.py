# Generated by Django 3.1.1 on 2020-09-04 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_on',
        ),
    ]
