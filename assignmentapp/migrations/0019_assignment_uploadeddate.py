# Generated by Django 4.2.8 on 2023-12-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignmentapp', '0018_alter_assignment_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='uploadedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
