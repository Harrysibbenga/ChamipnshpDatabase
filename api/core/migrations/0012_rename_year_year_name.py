# Generated by Django 3.2.3 on 2021-05-18 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_year_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='year',
            old_name='year',
            new_name='name',
        ),
    ]
