# Generated by Django 2.1.7 on 2019-03-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spayce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='receipt_value',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
