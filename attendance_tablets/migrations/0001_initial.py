# Generated by Django 3.2 on 2021-05-14 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceTablet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('store', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stores.store')),
            ],
        ),
    ]
