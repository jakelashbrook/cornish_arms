# Generated by Django 3.2 on 2022-02-28 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='model_name',
            field=models.CharField(default='About Us', max_length=20),
        ),
        migrations.AddField(
            model_name='food',
            name='model_name',
            field=models.CharField(default='Food Times', max_length=30),
        ),
        migrations.AddField(
            model_name='opening',
            name='model_name',
            field=models.CharField(default='Opening Times', max_length=40),
        ),
    ]
