# Generated by Django 4.1.2 on 2022-10-29 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_studentprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_type',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
