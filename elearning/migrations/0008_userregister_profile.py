# Generated by Django 4.0.6 on 2022-07-10 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0007_remove_userregister_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='Profile',
            field=models.ImageField(default='', upload_to='profile'),
        ),
    ]
