# Generated by Django 4.2.4 on 2023-10-05 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default='Active', max_length=8),
        ),
    ]
