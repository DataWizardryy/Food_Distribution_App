# Generated by Django 5.1.3 on 2024-11-25 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('area_of_service', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_description', models.TextField()),
                ('quantity', models.CharField(max_length=50)),
                ('available_until', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.donor')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_name', models.CharField(max_length=100)),
                ('requester_contact', models.CharField(max_length=15)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.fooditem')),
            ],
        ),
    ]
