# Generated by Django 4.2.8 on 2023-12-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignmentapp', '0015_alter_assignment_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='file',
            field=models.FileField(upload_to='assignments/'),
        ),
    ]
