# Generated by Django 4.0.5 on 2022-07-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_shares_sell_equity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='percentage_equity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
