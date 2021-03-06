# Generated by Django 3.2.9 on 2021-12-07 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('year', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('genres', models.CharField(blank=True, max_length=30, null=True)),
                ('summary', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'movie',
            },
        ),
    ]
