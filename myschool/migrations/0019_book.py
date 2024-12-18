# Generated by Django 5.1.3 on 2024-12-18 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0018_remove_instructor_courses_instructor_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(max_length=100)),
                ('language', models.CharField(default='English', max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('total_copies', models.PositiveIntegerField()),
                ('available_copies', models.PositiveIntegerField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='book_pdfs/')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]