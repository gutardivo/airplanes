# Generated by Django 4.2 on 2023-11-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=200)),
                ('profpic', models.ImageField(blank=True, null=True, upload_to='profile_pictures')),
            ],
        ),
    ]