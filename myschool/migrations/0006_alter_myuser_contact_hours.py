# Generated by Django 5.1.3 on 2025-01-07 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0005_alter_myuser_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='contact_hours',
            field=models.CharField(choices=[('1', '1 Hour'), ('2', '2 Hours'), ('3', '3 Hours'), ('4', '4 Hours'), ('5', '5 Hours'), ('6', '6 Hours'), ('4am-5am', '4:00 AM - 5:00 AM'), ('5am-6am', '5:00 AM - 6:00 AM'), ('6am-7am', '6:00 AM - 7:00 AM'), ('7am-8am', '7:00 AM - 8:00 AM'), ('8am-9am', '8:00 AM - 9:00 AM'), ('9am-10am', '9:00 AM - 10:00 AM'), ('10am-11am', '10:00 AM - 11:00 AM'), ('11am-12pm', '11:00 AM - 12:00 PM'), ('12pm-1pm', '12:00 PM - 1:00 PM'), ('1pm-2pm', '1:00 PM - 2:00 PM'), ('2pm-3pm', '2:00 PM - 3:00 PM'), ('3pm-4pm', '3:00 PM - 4:00 PM'), ('4pm-5pm', '4:00 PM - 5:00 PM'), ('5pm-6pm', '5:00 PM - 6:00 PM')], max_length=50),
        ),
    ]
