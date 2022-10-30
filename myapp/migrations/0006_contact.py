# Generated by Django 3.2.13 on 2022-10-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20220927_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('message', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
