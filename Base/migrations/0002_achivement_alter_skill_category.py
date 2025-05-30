# Generated by Django 5.1.7 on 2025-04-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('ac_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.CharField(choices=[('Languages', 'Language'), ('Frameworks', 'Framework'), ('Tools', 'Tool'), ('Courses', 'Course'), ('Soft Skills', 'Soft Skill')], max_length=50),
        ),
    ]
