# Generated by Django 5.1.3 on 2024-12-18 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0010_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='name',
            field=models.CharField(default='cs', max_length=255, verbose_name='comp'),
        ),
    ]
