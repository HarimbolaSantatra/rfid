# Generated by Django 3.1.3 on 2022-09-03 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RfidData',
        ),
        migrations.DeleteModel(
            name='UserData',
        ),
    ]