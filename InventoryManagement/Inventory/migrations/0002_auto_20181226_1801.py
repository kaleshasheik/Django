# Generated by Django 2.1.4 on 2018-12-26 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='first_login',
            new_name='must_change_password',
        ),
    ]