# Generated by Django 2.2.4 on 2019-08-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_painting_soldstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
