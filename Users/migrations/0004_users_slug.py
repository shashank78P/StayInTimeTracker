# Generated by Django 4.2.5 on 2023-11-26 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_users_passwordresetid'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
