# Generated by Django 5.1.3 on 2024-12-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='course_type',
            field=models.CharField(choices=[('cs', 'computer science'), ('machine learning', 'Ai'), ('web', 'web development'), ('software', 'software development'), ('forensic', 'ethical hacking'), ('bmc', 'com and maths'), ('bcom', 'commerce')], max_length=50, verbose_name='Course Type'),
        ),
    ]
