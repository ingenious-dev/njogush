
from rest_framework import serializers

from .models import (Project, Asset, Step, BuildSession)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'identifier', 'token', 'image', 'date_posted']

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'project', 'name', 'description', 'file', 'date_posted']

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'project', 'name', 'description', 'rank', 'category',
        'folder', 'file_path', 'asset', 'excerpt', 'excerpt_start', 'excerpt_end',
        'command', 'use_command_arguements',
        'is_suspended', 'date_posted']

class BuildSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildSession
        fields = ['id', 'project', 'logs', 'current_step', 'command_arguments', 'date_posted', 'date_modified']