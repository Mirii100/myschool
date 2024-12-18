# Generated by Django 5.1.3 on 2024-12-18 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0016_alter_instructor_specialization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('specialization_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('field', models.CharField(choices=[('Engineering', 'Engineering'), ('Science', 'Science'), ('Arts', 'Arts'), ('Business', 'Business'), ('Technology', 'Technology')], default='Technology', max_length=50)),
                ('popular_courses', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='specialization',
        ),
        migrations.AddField(
            model_name='instructor',
            name='specialization',
            field=models.ManyToManyField(related_name='instructors', to='myschool.specialization'),
        ),
    ]
