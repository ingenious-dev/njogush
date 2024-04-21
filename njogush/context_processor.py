from django.conf import settings


# TODO https://docs.djangoproject.com/en/4.2/ref/templates/api/#writing-your-own-context-processors
# def from_email(request):
#     return {
#         "DEFAULT_FROM_EMAIL": settings.DEFAULT_FROM_EMAIL,
#     }

def add_settings(request):
    return {
        "CUSTOM_SYSTEM_NAME": settings.CUSTOM_SYSTEM_NAME,

        "EMAIL_HOST_USER": settings.EMAIL_HOST_USER,
    }