# Generated by Django 3.2.3 on 2021-05-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_result_time_of_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date_of_event',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='result',
            name='time_of_event',
            field=models.CharField(max_length=50),
        ),
    ]
