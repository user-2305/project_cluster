# Generated by Django 5.0.2 on 2024-02-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('indicator', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
