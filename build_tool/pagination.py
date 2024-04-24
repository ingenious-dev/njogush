from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# + https://www.django-rest-framework.org/api-guide/pagination/#setup
class VariableResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    # max_page_size = 50