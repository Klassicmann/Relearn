# Generated by Django 4.1.2 on 2022-10-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
