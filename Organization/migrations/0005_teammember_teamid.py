# Generated by Django 4.2.5 on 2023-11-30 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0004_teammember_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='TeamId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Organization.team'),
        ),
    ]