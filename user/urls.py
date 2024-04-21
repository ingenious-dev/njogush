from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'
urlpatterns =[
    # path('register', views.register, name='register'), # this functionality is only available at '/install'

    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(success_url='/user/password_reset/done'),
        name="password_reset"
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(success_url='/user/reset/done'),
        name="password_reset_complete"
    ),

    path('', include('django.contrib.auth.urls')), #https://docs.djangoproject.com/en/4.0/topics/auth/default/#using-the-views
]


from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns(urlpatterns)

# https://www.django-rest-framework.org/api-guide/authentication/#generating-tokens
from rest_framework.authtoken import views as views_framework
urlpatterns += [
    path('api-token-auth/', views_framework.obtain_auth_token)
]

from . import view_drf
urlpatterns += [
    path('api-token-auth/v2/', view_drf.obtain_auth_token)
]