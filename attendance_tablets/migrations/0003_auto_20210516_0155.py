# Generated by Django 3.2 on 2021-05-16 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance_tablets', '0002_alter_attendancetablet_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancetablet',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attendancetablet',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]
