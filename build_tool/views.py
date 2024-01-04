from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import (Project_Form, Asset_Form, Step_Form,)
from .view_drf import *
# Create your views here.

def index(request):
    context = {}

    return render( request, 'build_tool_vue/dist/index.html', context)