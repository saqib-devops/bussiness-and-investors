# Generated by Django 4.0.5 on 2022-06-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
