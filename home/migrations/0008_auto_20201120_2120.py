# Generated by Django 3.1.2 on 2020-11-20 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201120_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='postedby',
            new_name='user_name',
        ),
    ]