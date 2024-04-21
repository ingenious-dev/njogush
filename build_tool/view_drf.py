
from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied, ParseError, ValidationError

from .models import (Project, Asset, Step, BuildSession)
from .serializers import (ProjectSerializer, AssetSerializer, StepSerializer, BuildSessionSerializer)

@api_view(['GET'])
def dashboard(request):
    data = {}
    
    data['projects_count'] = Project.objects.count()
    data['assets_count'] = Asset.objects.count()
    data['build_sessions_count'] = BuildSession.objects.count()

    last_build_sessions = BuildSession.objects.all().order_by('date_modified')[:10]
    serializer = BuildSessionSerializer(last_build_sessions, many=True)

    data['last_build_sessions'] = serializer.data

    return Response(data)

# ! PROJECT
class ProjectList(generics.ListCreateAPIView):
    """
    List all Project or create a new Project.
    """

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Project.objects.all().order_by('-id')
        return queryset

    def filter_queryset(self, queryset):
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name=name)

        identifier = self.request.query_params.get('identifier')
        if identifier:
            queryset = queryset.filter(identifier=identifier)

        return queryset

    def get_serializer_class(self):
        return ProjectSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update, Delete, or View a Project
    """

    def get_serializer_class(self):
        return ProjectSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Project.objects.all()
        return queryset

    # https://www.django-rest-framework.org/tutorial/3-class-based-views/#rewriting-our-api-using-class-based-views
    def patch(self, request, pk, format=None):
        # resource = self.get_object(pk)
        resource = self.get_object() # + https://www.django-rest-framework.org/api-guide/generic-views/#get_objectself
        serializer = self.get_serializer_class()(resource, data=request.data, partial=True) # + https://www.django-rest-framework.org/api-guide/serializers/#partial-updates
        if serializer.is_valid():
            resource.status = request.data.get('action')

            if request.data.get('action') == 'run':
                host = request.get_host()
                if '127.0.0.1' not in host and 'localhost' not in host:
                    if not settings.REMOTE_MODE:
                        raise ValidationError('Remote executions are not allowed.')
                    
                build_session = BuildSession.objects.create(
                    project = resource,
                )
                build_serializer = BuildSessionSerializer(build_session)
                return Response(build_serializer.data)
            
            if request.data.get('action') == 'reconfigure':
                Asset.objects.filter(project=resource).delete()
                Step.objects.filter(project=resource).delete()
                # resource.build_sessions.delete()
                # TO BE DONE - which build_session again?
                # self.build_session.logs = ''
                # self.build_session.current_step = None
                # self.build_session.save()
            
            if request.data.get('action'):
                resource.save()
            else:
                serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_update(self, serializer):
        instance = serializer.save()

# ! ASSET
class AssetList(generics.ListCreateAPIView):
    """
    List all Asset or create a new Asset.
    """

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Asset.objects.all().order_by('-id')
        return queryset

    def filter_queryset(self, queryset):
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name=name)

        project = self.request.query_params.get('project')
        if project:
            queryset = queryset.filter(project=project)

        return queryset

    def get_serializer_class(self):
        return AssetSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

class AssetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update, Delete, or View a Asset
    """

    def get_serializer_class(self):
        return AssetSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Asset.objects.all()
        return queryset

    def perform_update(self, serializer):
        file = serializer.validated_data.get("file")
        if file:
            resource = self.get_object()
            resource.file.delete()
            
        instance = serializer.save()

# ! STEP
class StepList(generics.ListCreateAPIView):
    """
    List all Step or create a new Step.
    """

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Step.objects.all().order_by('-id')
        return queryset

    def filter_queryset(self, queryset):
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name=name)

        project = self.request.query_params.get('project')
        if project:
            queryset = queryset.filter(project=project).order_by('rank')

        return queryset

    def get_serializer_class(self):
        return StepSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

class StepDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update, Delete, or View a Step
    """

    def get_serializer_class(self):
        return StepSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Step.objects.all()
        return queryset

    def perform_update(self, serializer):
        instance = serializer.save()

# ! BUILD SESSION
class BuildSessionList(generics.ListCreateAPIView):
    """
    List all BuildSession or create a new BuildSession.
    """

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = BuildSession.objects.all().order_by('-id')
        return queryset

    def filter_queryset(self, queryset):
        project = self.request.query_params.get('project')
        if project:
            queryset = queryset.filter(project=project)

        return queryset

    def get_serializer_class(self):
        return BuildSessionSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

class BuildSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update, Delete, or View a BuildSession
    """

    def get_serializer_class(self):
        return BuildSessionSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = BuildSession.objects.all()
        return queryset

    def perform_update(self, serializer):
        instance = serializer.save()

# TODO https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#creating-an-endpoint-for-the-root-of-our-api
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    if not settings.DEBUG:
        raise PermissionDenied(detail="API discovery not allowed at this time")

    return Response({
        'projects': reverse('build_tool:project-list', request=request, format=format),
        'assets': reverse('build_tool:asset-list', request=request, format=format),
        'steps': reverse('build_tool:step-list', request=request, format=format),
        'build-sessions': reverse('build_tool:build-session-list', request=request, format=format),
    })