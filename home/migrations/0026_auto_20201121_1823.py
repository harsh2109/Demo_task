# Generated by Django 3.1.2 on 2020-11-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20201121_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(default='', upload_to='questions/'),
        ),
    ]
