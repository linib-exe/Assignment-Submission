# Generated by Django 4.2.8 on 2023-12-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignmentapp', '0014_alter_assignment_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='assignments/'),
        ),
    ]
