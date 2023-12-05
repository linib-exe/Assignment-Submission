# Generated by Django 4.2.8 on 2023-12-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('faculty', models.CharField(choices=[('BIT', 'BIT'), ('B.Sc CSIT', 'B.Sc CSIT')], max_length=10)),
                ('rollno', models.CharField(max_length=15)),
                ('semester', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], max_length=10)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=10)),
            ],
        ),
    ]