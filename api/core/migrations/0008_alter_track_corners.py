# Generated by Django 3.2.3 on 2021-05-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210518_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='corners',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
