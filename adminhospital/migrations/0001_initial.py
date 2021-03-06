# Generated by Django 3.1.1 on 2020-09-06 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('specialty', models.CharField(max_length=30)),
                ('medic_id', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=2)),
                ('dni', models.IntegerField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.DateTimeField()),
                ('date', models.DateField()),
                ('medic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminhospital.medic')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminhospital.person')),
            ],
        ),
    ]
