# Generated by Django 4.2.1 on 2023-05-22 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EMSAPI', '0002_register_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_login',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='register_login',
            old_name='lname',
            new_name='last_name',
        ),
    ]
