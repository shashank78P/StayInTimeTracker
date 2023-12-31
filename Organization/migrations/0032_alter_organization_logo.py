# Generated by Django 4.2.5 on 2023-12-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0031_organization_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(default='organization.png', error_messages={'invalid': 'Invalid file (file is not acceptable).'}, max_length=20000, upload_to='organizationLogo'),
        ),
    ]
