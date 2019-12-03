from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Todos
# Create your views here.

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def main(request):
    todos = Todos.objects.all()
    todos_list = serializers.serialize('json', todos)

    return HttpResponse(todos_list, content_type='text/json-comment-filtered')