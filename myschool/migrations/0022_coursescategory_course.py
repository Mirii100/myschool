# Generated by Django 5.1.3 on 2024-12-25 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0021_coursescategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursescategory',
            name='course',
            field=models.ForeignKey(default=[('cs', 'Computer Science'), ('ai', 'Artificial Intelligence'), ('ml', 'Machine Learning'), ('ds', 'Data Science'), ('web_dev', 'Web Development'), ('app_dev', 'Mobile Application Development'), ('cybersec', 'Cyber Security'), ('ethical_hacking', 'Ethical Hacking'), ('software_dev', 'Software Development'), ('networking', 'Computer Networking'), ('cloud_computing', 'Cloud Computing'), ('iot', 'Internet of Things (IoT)'), ('blockchain', 'Blockchain Technology'), ('devops', 'DevOps'), ('bcom', 'Commerce'), ('mba', 'Master of Business Administration'), ('accounting', 'Accounting and Finance'), ('marketing', 'Marketing'), ('hrm', 'Human Resource Management'), ('entrepreneurship', 'Entrepreneurship'), ('economics', 'Economics'), ('literature', 'English Literature'), ('history', 'History'), ('philosophy', 'Philosophy'), ('psychology', 'Psychology'), ('sociology', 'Sociology'), ('political_science', 'Political Science'), ('linguistics', 'Linguistics'), ('fine_arts', 'Fine Arts'), ('music', 'Music'), ('film_studies', 'Film Studies'), ('design', 'Graphic Design'), ('math', 'Mathematics'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('biology', 'Biology'), ('geology', 'Geology'), ('statistics', 'Statistics'), ('environmental_science', 'Environmental Science'), ('biotech', 'Biotechnology'), ('astrophysics', 'Astrophysics'), ('mech_eng', 'Mechanical Engineering'), ('civil_eng', 'Civil Engineering'), ('elec_eng', 'Electrical Engineering'), ('elec_comm_eng', 'Electronics and Communication Engineering'), ('chemical_eng', 'Chemical Engineering'), ('aero_eng', 'Aerospace Engineering'), ('biomed_eng', 'Biomedical Engineering'), ('robotics', 'Robotics Engineering'), ('medicine', 'Medicine'), ('nursing', 'Nursing'), ('pharmacy', 'Pharmacy'), ('dentistry', 'Dentistry'), ('physiotherapy', 'Physiotherapy'), ('public_health', 'Public Health'), ('law', 'Law'), ('criminology', 'Criminology'), ('forensics', 'Forensic Science'), ('international_relations', 'International Relations'), ('public_admin', 'Public Administration'), ('education', 'Education'), ('sports_science', 'Sports Science'), ('hospitality', 'Hospitality Management'), ('tourism', 'Tourism and Travel'), ('culinary_arts', 'Culinary Arts'), ('journalism', 'Journalism and Mass Communication'), ('fashion_design', 'Fashion Design'), ('animation', 'Animation'), ('agriculture', 'Agriculture'), ('marine_biology', 'Marine Biology'), ('veterinary', 'Veterinary Science'), ('ai_ml', 'Artificial Intelligence & Machine Learning')], on_delete=django.db.models.deletion.CASCADE, to='myschool.courses'),
        ),
    ]
