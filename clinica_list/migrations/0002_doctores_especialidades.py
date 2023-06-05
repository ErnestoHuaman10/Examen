# Generated by Django 4.2.1 on 2023-06-05 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctores',
            fields=[
                ('doctor_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('doctor_nombre', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'doctores',
            },
        ),
        migrations.CreateModel(
            name='especialidades',
            fields=[
                ('especialidad_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('especialidad_nombre', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'especialidades',
            },
        ),
    ]
