# Generated by Django 5.1.2 on 2024-11-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='Media/Profile_pic'),
        ),
    ]
