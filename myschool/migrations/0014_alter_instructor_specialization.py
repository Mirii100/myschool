# Generated by Django 5.1.3 on 2024-12-18 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0013_alter_instructor_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='specialization',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myschool.signup'),
        ),
    ]