# Generated by Django 5.0.4 on 2024-05-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_totalcalories_emailid'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalcalories',
            name='date',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
