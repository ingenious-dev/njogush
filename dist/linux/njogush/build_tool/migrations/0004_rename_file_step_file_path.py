# Generated by Django 4.2.8 on 2023-12-29 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build_tool', '0003_step_category_step_command_alter_asset_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='step',
            old_name='file',
            new_name='file_path',
        ),
    ]
