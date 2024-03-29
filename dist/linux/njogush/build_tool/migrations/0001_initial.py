# Generated by Django 4.2.8 on 2023-12-29 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('file', models.FileField(upload_to='asset_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('rank', models.IntegerField()),
                ('folder', models.TextField(blank=True)),
                ('file', models.TextField(blank=True)),
                ('excerpt', models.TextField(blank=True)),
                ('excerpt_start', models.CharField(blank=True, max_length=100)),
                ('excerpt_end', models.CharField(blank=True, max_length=100)),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='build_tool.asset')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='build_tool.project')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='build_tool.project'),
        ),
    ]
