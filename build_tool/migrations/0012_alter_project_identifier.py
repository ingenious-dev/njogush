# Generated by Django 4.2.8 on 2024-01-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_tool', '0011_auto_20240113_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='identifier',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]