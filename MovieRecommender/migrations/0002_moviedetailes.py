# Generated by Django 4.2.11 on 2024-03-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieRecommender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDetailes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('image', models.ImageField(upload_to='Movies')),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateField(max_length=250)),
                ('actors', models.CharField(max_length=250)),
                ('genres', models.CharField(max_length=250)),
                ('trailer_link', models.EmailField(max_length=250, unique=True)),
            ],
        ),
    ]
