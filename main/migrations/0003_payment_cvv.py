# Generated by Django 2.2.4 on 2019-08-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190812_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cvv',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]