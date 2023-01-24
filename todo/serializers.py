from rest_framework import serializers

class TaskExecutionSerializer(serializers.Serializer):
    assignee_id = serializers.IntegerField()
    task_count = serializers.IntegerField()
