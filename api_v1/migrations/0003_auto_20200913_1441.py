# Generated by Django 2.1.5 on 2020-09-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0002_remove_subjects_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=100),
        ),
    ]