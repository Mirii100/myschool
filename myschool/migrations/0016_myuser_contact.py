# Generated by Django 5.1.3 on 2025-01-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0015_myuser_gender_myuser_nationality_myuser_reg_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='contact',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
