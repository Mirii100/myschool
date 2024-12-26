# Generated by Django 5.1.3 on 2024-12-25 15:05

import django.db.models.deletion
import myschool.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0022_coursescategory_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursescategory',
            name='course',
            field=models.ForeignKey(default=myschool.models.courses, on_delete=django.db.models.deletion.CASCADE, to='myschool.courses'),
        ),
    ]
