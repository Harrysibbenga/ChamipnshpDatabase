# Generated by Django 3.2.3 on 2021-05-17 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
