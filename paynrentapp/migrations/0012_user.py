# Generated by Django 4.1.6 on 2023-06-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0011_vehicle_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='', max_length=70)),
                ('UserEmail', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=150)),
                ('mobileno', models.CharField(default='', max_length=15)),
                ('AadharNumber', models.CharField(default='', max_length=15)),
                ('licenceNumber', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
