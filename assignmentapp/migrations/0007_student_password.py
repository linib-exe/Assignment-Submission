# Generated by Django 4.2.8 on 2023-12-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignmentapp', '0006_alter_student_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
