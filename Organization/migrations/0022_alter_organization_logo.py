# Generated by Django 4.2.5 on 2023-12-10 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0021_alter_organization_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.CharField(default='organization.png', error_messages={'invalid': 'Invalid file (file is not acceptable).'}, max_length=10000),
        ),
    ]
