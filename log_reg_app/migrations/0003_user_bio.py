# Generated by Django 2.2 on 2020-08-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg_app', '0002_auto_20200808_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.CharField(max_length=255, null=True),
        ),
    ]