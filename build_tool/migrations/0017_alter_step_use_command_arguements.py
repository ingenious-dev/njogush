# Generated by Django 4.2.8 on 2025-02-06 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_tool', '0016_step_use_command_arguements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='use_command_arguements',
            field=models.BooleanField(default=False),
        ),
    ]
