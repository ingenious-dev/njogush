# Generated by Django 4.2.8 on 2023-12-30 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build_tool', '0005_buildsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildsession',
            name='current_step',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='build_tool.step'),
        ),
    ]
