# Generated by Django 3.2.9 on 2021-11-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_alter_rollnumber_rollno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rollnumber',
            name='time',
        ),
        migrations.AddField(
            model_name='rollnumber',
            name='branch',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='rollnumber',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
