# Generated by Django 4.0.6 on 2022-07-10 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0006_alter_userregister_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregister',
            name='IMAGE',
        ),
    ]
