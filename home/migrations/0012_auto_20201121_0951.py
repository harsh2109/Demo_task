# Generated by Django 3.1.2 on 2020-11-21 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201121_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='user_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
