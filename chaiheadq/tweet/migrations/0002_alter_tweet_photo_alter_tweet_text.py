# Generated by Django 5.2 on 2025-04-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='tweets/'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(),
        ),
    ]
