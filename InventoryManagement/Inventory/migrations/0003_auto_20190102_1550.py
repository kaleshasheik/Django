# Generated by Django 2.1.4 on 2019-01-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_auto_20190102_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterModelTable(
            name='inventory',
            table='Inventory_Types',
        ),
    ]
