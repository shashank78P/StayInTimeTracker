# Generated by Django 4.2.5 on 2023-11-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
            ],
        ),
    ]
