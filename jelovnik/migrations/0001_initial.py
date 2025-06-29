# Generated by Django 5.2.3 on 2025-06-16 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('opis', models.TextField(blank=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=6)),
                ('posno', models.BooleanField(default=False)),
                ('preporuceno', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VrstaJela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dodatak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
                ('jela', models.ManyToManyField(blank=True, related_name='dodaci', to='jelovnik.jelo')),
            ],
        ),
        migrations.AddField(
            model_name='jelo',
            name='vrsta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jela', to='jelovnik.vrstajela'),
        ),
    ]
