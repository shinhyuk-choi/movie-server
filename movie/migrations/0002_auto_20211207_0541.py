# Generated by Django 3.2.9 on 2021-12-07 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_yts',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
