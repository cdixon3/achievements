from urllib import response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TaskExecution
from .serializers import TaskExecutionSerializer

# Create your views here.

@api_view()
def task_execution_list(request):
    result = (TaskExecution.objects.filter(status='SUCCEEDED').values('assignee_id').annotate(task_count=Count('assignee_id')).order_by())

    serializer = TaskExecutionSerializer(result, many=True)

    return Response(serializer.data)
