# Generated by Django 4.2.8 on 2024-06-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_tool', '0013_step_is_suspended'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildsession',
            name='command_arguements',
            field=models.TextField(blank=True),
        ),
    ]
