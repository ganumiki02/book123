# Generated by Django 4.0.2 on 2022-03-29 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=200)),
                ('suggestions', models.TextField(default='', max_length=200)),
            ],
        ),
    ]
