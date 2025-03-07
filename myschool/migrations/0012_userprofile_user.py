# Generated by Django 5.1.3 on 2025-01-07 18:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def set_user_for_userprofile(apps, schema_editor):
    # Get the User and UserProfile models
    User = apps.get_model('auth', 'User')
    UserProfile = apps.get_model('myschool', 'UserProfile')

    # Get the logged-in user (this may require custom logic to obtain the user)
    logged_in_user = User.objects.get(username='your_logged_in_username')  # Replace with actual logic

    # Update the user field for existing rows
    UserProfile.objects.filter(user__isnull=True).update(user=logged_in_user)

class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0011_userprofile_course'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(set_user_for_userprofile),
    ]
