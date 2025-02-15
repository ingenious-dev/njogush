from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    identifier = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='project_pic', null=True, blank=True)
    token = models.TextField(null=True, blank=True, unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class Asset(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='assets')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='asset_file')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Step(models.Model):
    CATEGORY_CHOICES = (
        ('folder', 'Folder'),
        ('file', 'File'),
        ('excerpt', 'Excerpt'),
        ('command', 'Command'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    rank = models.IntegerField()
    
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    # FOLDER
    folder = models.TextField(blank=True)
    # FILE
    file_path = models.TextField(blank=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, null=True, blank=True)
    # EXCERPT
    excerpt = models.TextField(blank=True)
    excerpt_start = models.CharField(max_length=100, blank=True)
    excerpt_end = models.CharField(max_length=100, blank=True)
    # COMMAND
    command = models.TextField(blank=True)
    
    # <<<<<<<<<>>>>>>>>>>
    # You have to opt in so that it does not affect usual behavaviour
    use_command_arguements = models.BooleanField(default=False)
    # <<<<<<<<<>>>>>>>>>>

    is_suspended = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class BuildSession(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='build_sessions')
    logs = models.TextField(blank=True)
    current_step = models.ForeignKey(Step, on_delete=models.CASCADE, null=True, blank=True)
    command_arguments = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)