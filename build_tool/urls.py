from django.urls import path, include, re_path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'build_tool'
urlpatterns = [
    path('install', views.install, name='install'),

    path('', views.index, name='index'),

    # TODO https://stackoverflow.com/a/6259570/10401826
    # for non-api calls take them to vue app to avoid 404 errors when you reload the browser
    re_path(r'^(?!api|media|static).*$', views.index, name='remaining_urls'),
]

urlpatterns += [
    path('api/', views.api_root),

    path('api/dashboard/', views.dashboard, name='dashboard'),

    path('api/projects/', views.ProjectList.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),

    path('api/assets/', views.AssetList.as_view(), name='asset-list'),
    path('api/assets/<int:pk>/', views.AssetDetail.as_view(), name='asset-detail'),

    path('api/steps/', views.StepList.as_view(), name='step-list'),
    path('api/steps/<int:pk>/', views.StepDetail.as_view(), name='step-detail'),

    path('api/build-sessions/', views.BuildSessionList.as_view(), name='build-session-list'),
    path('api/build-sessions/<int:pk>/', views.BuildSessionDetail.as_view(), name='build-session-detail'),

    path('api/github_callback/<int:pk>/<token>/', views.github_callback, name='github-callback'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)