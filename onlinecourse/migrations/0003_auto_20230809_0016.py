# Generated by Django 3.1.3 on 2023-08-09 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20230707_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='chocies',
            new_name='choices',
        ),
    ]