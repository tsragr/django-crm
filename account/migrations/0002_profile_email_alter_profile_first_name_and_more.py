# Generated by Django 4.0 on 2021-12-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='Ivan', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='patronymic',
            field=models.CharField(default='Ivanovich', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='second_name',
            field=models.CharField(default='Ivanov', max_length=100),
        ),
    ]
