# Generated by Django 3.1.2 on 2020-11-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20201121_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='image',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]