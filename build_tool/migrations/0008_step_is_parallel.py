# Generated by Django 4.2.8 on 2024-01-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_tool', '0007_buildsession_date_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='is_parallel',
            field=models.BooleanField(default=False),
        ),
    ]
