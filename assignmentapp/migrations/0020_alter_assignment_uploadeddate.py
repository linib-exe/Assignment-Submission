# Generated by Django 4.2.8 on 2023-12-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignmentapp', '0019_assignment_uploadeddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='uploadedDate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
