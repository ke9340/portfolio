# Generated by Django 5.1.7 on 2025-04-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0005_alter_education_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='location',
            field=models.CharField(default='India', max_length=30, null=True),
        ),
    ]
