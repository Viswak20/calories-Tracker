# Generated by Django 5.0.4 on 2024-05-17 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0013_remove_totalcalories_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalcalories',
            name='date',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
