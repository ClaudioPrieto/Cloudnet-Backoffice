# Generated by Django 3.2.4 on 2021-06-13 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('point_of_sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('model_number', models.CharField(max_length=120)),
                ('brand', models.CharField(max_length=120)),
                ('os', models.CharField(max_length=120)),
                ('color', models.CharField(max_length=120)),
                ('memory', models.PositiveIntegerField()),
                ('internal_memory', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('sale', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('point_of_sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='point_of_sales.pointofsale')),
            ],
        ),
    ]