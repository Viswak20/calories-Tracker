# Generated by Django 5.0.4 on 2024-04-30 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_totalcaloriescalculate_finalcalories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='totalcaloriescalculate',
            old_name='name',
            new_name='mailid',
        ),
    ]
