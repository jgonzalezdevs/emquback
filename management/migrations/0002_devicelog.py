# Generated by Django 3.2.16 on 2022-10-21 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_answered', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.device')),
            ],
        ),
    ]
