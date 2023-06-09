# Generated by Django 4.0.3 on 2023-04-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.IntegerField(max_length=6)),
                ('message', models.TextField(max_length=400)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
