# Generated by Django 5.1.3 on 2024-12-17 18:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0006_testimonial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='status',
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(upload_to='testimonials/'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]