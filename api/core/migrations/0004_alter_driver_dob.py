# Generated by Django 3.2.3 on 2021-05-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210518_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]