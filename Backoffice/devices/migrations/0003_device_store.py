# Generated by Django 3.2 on 2021-05-11 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
        ('devices', '0002_alter_device_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stores.store'),
        ),
    ]