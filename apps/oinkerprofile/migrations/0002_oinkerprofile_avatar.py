# Generated by Django 3.1 on 2020-09-01 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oinkerprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oinkerprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]